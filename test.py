

import os
import wave
from array import array
from struct import pack
from sys import byteorder
import librosa
import numpy as np
import pyaudio
import speech_recognition as sr
import copy

THRESHOLD = 800 # audio levels not normalised.import 
CHUNK_SIZE = 1024
SILENT_CHUNKS = 3 * 44100 / 1024  # about 3sec
FORMAT = pyaudio.paInt16
FRAME_MAX_VALUE = 2 ** 15 - 1
NORMALIZE_MINUS_ONE_dB = 10 ** (-1.0 / 20)
RATE = 44100
CHANNELS = 1
TRIM_APPEND = RATE / 4

def is_silent(data_chunk):
    """Returns 'True' if below the 'silent' threshold"""
    return max(data_chunk) < THRESHOLD

def normalize(data_all):
    """Amplify the volume out to max -1dB"""
    # MAXIMUM = 16384
    normalize_factor = (float(NORMALIZE_MINUS_ONE_dB * FRAME_MAX_VALUE)
                        / max(abs(i) for i in data_all))

    r = array('h')
    for i in data_all:
        r.append(int(i * normalize_factor))
    return r

def trim(data_all):
    _from = 0
    _to = len(data_all) - 1
    for i, b in enumerate(data_all):
        if abs(b) > THRESHOLD:
            _from = max(0, i - TRIM_APPEND)
            break

    for i, b in enumerate(reversed(data_all)):
        if abs(b) > THRESHOLD:
            _to = min(len(data_all) - 1, len(data_all) - 1 - i + TRIM_APPEND)
            break

    return copy.deepcopy(data_all[int(_from):(int(_to) + 1)])

def record():
    """Record a word or words from the microphone and 
    return the data as an array of signed shorts."""

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, output=True, frames_per_buffer=CHUNK_SIZE)

    silent_chunks = 0
    audio_started = False
    data_all = array('h')

    while True:
        # little endian, signed short
        data_chunk = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            data_chunk.byteswap()
        data_all.extend(data_chunk)

        silent = is_silent(data_chunk)

        if audio_started:
            if silent:
                silent_chunks += 1
                if silent_chunks > SILENT_CHUNKS:
                    break
            else: 
                silent_chunks = 0
        elif not silent:
            audio_started = True              

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()
    data_all = normalize(data_all)
    data_all = trim(data_all) 

    return sample_width, data_all

def record_to_file(path):
    # "Records from the microphone and outputs the resulting data to 'path'"
    sample_width, data = record()
    data = pack('<' + ('h' * len(data)), *data)

    wave_file = wave.open(path, 'wb')
    wave_file.setnchannels(CHANNELS)
    wave_file.setsampwidth(sample_width)
    wave_file.setframerate(RATE)
    wave_file.writeframes(data)
    wave_file.close()

# channels = 1  # Set Mono for audio
# sample_rate = 44100  
# def record_to_file(audio):
#                                       # "Records from the microphone and outputs the resulting data to 'path'"
#     frames = audio.get_raw_data()
    
#     with wave.open("recorded.wav", "wb") as wf:
#         wf.setnchannels(channels)
#         wf.setsampwidth(audio.sample_width)
#         wf.setframerate(sample_rate)
#         wf.writeframes(frames)


def extract_feature(file_name):
 
    X, sample_rate = librosa.core.load(file_name)
    result = np.array([])

    mel = np.mean(librosa.feature.melspectrogram(y=X, sr=sample_rate).T,axis=0)
    result = np.hstack((result, mel))
  
    return result



def listen():
        
      
      samples=os.listdir('test-samples')
      i=-1
      length=len(samples)
      while 1:
        file=''
        if len(samples) != 0:
          i=i+1
          if length!=0:
           file = 'test-samples\\'+samples[i]
           length=length-1
           print(samples[i])
          else:
            break
   
        if len(samples)==0:
  
         if not file or not os.path.isfile(file):
            i=-1
            print("Please talk")

            file='recorded.wav'

            record_to_file(file)
                    
            r = sr.Recognizer()
            
            with sr.AudioFile(file) as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source,duration=1)
                audio = r.listen(source,None,90)
            
            try:
                print("Recoginizing...")
                query = r.recognize_google(audio, language='en-in')
                print(f"User said: {query}\n")
                
        
            except Exception as e:
                print("Say that again please...")
                listen()

        features = extract_feature(file).reshape(1, -1)
       
        male_prob = model.predict(features)[0][0]
        female_prob = 1 - male_prob
      
        if male_prob > female_prob:
         gender = "male" 
        else :
         gender = "female"
        
        print("Gender:", gender)
        print(f"Male: {male_prob*100:.2f}%  \nFemale: {female_prob*100:.2f}%") 
       


if __name__=="__main__":

    from utils import create_model
        
    
    model = create_model()
    model.load_weights("C:/xampp/htdocs/php/Projects/voice assistant/results/model.h5")
    listen()

        

     