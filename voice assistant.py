
import datetime
import os
import random
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import wave
from test import record_to_file, extract_feature
from utils import create_model
    
model = create_model()
model.load_weights("results\\model.h5")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[-1].id)
engine.setProperty('rate',150) 

def speak(text):
   print(text)
   engine.say(text)
   engine.runAndWait()


# channels = 1  # Set Mono for audio
# sample_rate = 40000  # audio sample
# def record_to_file(audio):
#                                       # "Records from the microphone and outputs the resulting data to 'path'"
#     frames = audio.get_raw_data()
    
#     with wave.open("recorded.wav", "wb") as wf:
#         wf.setnchannels(channels)
#         wf.setsampwidth(audio.sample_width)
#         wf.setframerate(sample_rate)
#         wf.writeframes(frames)


def Gender():
    file='recorded.wav'
    features = extract_feature(file).reshape(1, -1)
       
    male_prob = model.predict(features)[0][0]
    female_prob = 1 - male_prob
      
    if male_prob > female_prob:
       return "Sir" 
    else :
        return "Mam"
    
    
def Name():
   return 'Cortana'
   

def S1():
        e=random.randint(0,2)
        if e==0:
         c=f"{Gender()}! sorry to interrupt you but its"
        elif e==1:
         c=f"{Gender()}! It's {Time()}. So, it must be "
        elif e==2:
         c=f"{Gender()}! its "
        return c
    
def S2():
        e=random.randint(0,5)
        if e==0:
         c="Please tell me, how may I help you?"
        elif e==1:
         c="How can I help?" 
        elif e==2:
         c="Is there something I can do for you?"
        elif e==3:
         c="How may I assist you?"    
        elif e==4:
         c="Feel free to ask me if you need something."  
        elif e==5:
         c="Want me to help you with something?"   
        return c


def day():
     hour=int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
       a="morning"
     elif hour>=12 and hour<18: 
       a="afternoon"
     else:
       a="evening"
     return a  
 
def wishMe(start): 
  
    if f'{day()}' in start:
       a=f"Good {day()} {Gender()}! {S2()}"
       speak(a)

    elif not f'{day()}' in start:
       a=f"{S1()} {day()}. Anyway, {S2()}" 
       speak(a)

    else:
        b=0
        callAssistant(b) 
    return a
  
def callAssistant(b):
    while 1:
     start=takeCommand(b).lower()
     
     if 'hello' in start or f'hi' in start and f'{Name()}' in start:
        speak(f"Good {day()} {Gender()}! {S2()}")
        main() 

     elif f'good' in start or f'{Name()}' in start:
        wishMe(start)
        main()

def Sleep(query):
 while 1:
    if f'hold on {Name()}' in query or f'go sleep' in query or f'take a break {Name()}' in query:
     a=random.randint(0,2)
     if a==0 :
      speak(f"Ok {Gender()}, Going to sleep....")
     elif a==1 :
      speak(f"Ok {Gender()}, Leaving out....")      
     elif a==2 :
      speak(f"Ok {Gender()}, Logging out....")  
      
      
    elif f'get up {Name()}' in query or f'wake up {Name()}' in query:
       print("Logging in....")
       a=f" Good {day()} {Gender()}! "
       speak(a)

    elif f"good " in query:
      if f'{day()}' in query:
       a=f"Good {day()} {Gender()}!"
       speak(a)
      elif not f'{day()}' in query:
       a=f"{S1()} {day()}." 
       speak(a)

      else:
        b=0
        callAssistant(b) 
      main()

    b=0
    query=takeCommand(b).lower()



    

def takeCommand(b=0):
    #It takes microphone input from the user and returns string output
    file='recorded.wav'
    query=''
    
    print("Listening...")
    record_to_file(file)
                    
    # mic = sr.Microphone(device_index=1)
    r = sr.Recognizer()
    # with mic as source:
    #   print("Listening...")
    #   r.adjust_for_ambient_noise(source)
    #   audio = r.listen(source)
      
    #   record_to_file(audio)

  
    with sr.AudioFile(file) as source:
       
        r.adjust_for_ambient_noise(source,duration=1)
        
        audio = r.listen(source,None,6)   
    
    try:
            print("Recoginizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
   
    except Exception as e:
        # print(e)
       print("Say that again please...")
       
    return query

def Time():
    str=datetime.datetime.now().strftime("%H")
    hour = int(str)
    if hour > 12:
        day="PM"
        hour=hour-12
    elif hour==0:
        hour=12
        day="AM"
    else:
        day="AM"

    strmin = datetime.datetime.now().strftime("%M")
    a=f"{hour}:{strmin}, {day}"    

    return a

def Date_Time(query):
    a = ""
    arr = ['what','tell', 'show', 'display']

    if any(word in query for word in arr) and 'year' in query:
       a=datetime.datetime.now().strftime("it's %Y")
    elif any(word in query for word in arr) and 'month' in query:
       a=datetime.datetime.now().strftime("it's %B")
    elif any(word in query for word in arr) and 'date' in query:
       a=datetime.datetime.now().strftime("Today's date is %d:%B:%Y, %A")  
    elif any(word in query for word in arr) and 'time' in query:
       a=f"it's {Time()}"
    elif any(word in query for word in arr) and ('day' in query or 'week' in query):
       a=datetime.datetime.now().strftime("Today is %D and week is %A")
    return a

def main():
        
        b=0


        while True:
            
            query = takeCommand(b).lower()
            
            # Logic for executing tasks based on query
            if 'good morning' in query or 'good evening' in query or 'good' in query:
                   wishMe(query)
                   main()
            elif 'search' in query:
                    speak('Searching wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    speak(results)
                    
            elif 'open browser' in query:
                
                if 'open browser' == query:   
                   speak('what you want to search')
                   query=takeCommand(b).lower()
                   webbrowser.open(f"{query}")
                   main()

                elif 'browser search ' in query:
                    c=query.split("search ",1)
                    query=c[1]
                    print()
                    webbrowser.open(f"{query} ",new=0)
                    main()
            
                
                       
            elif 'close browser' in query or 'stop browser' in query or 'turn off browser' in query:
                 os.system("TASKKILL /F /IM msedge.exe")
                     
                 
            elif 'time' in query or 'date' in query or 'day' in query or 'year' in query or'month' in query:
                a=Date_Time(query)

                print(f'{Gender()}, {a}')
                speak(a)

            elif 'nice' in query or 'well done' in query or 'good job' in query or 'Excellent Work' in query:
                a=f"Thanks for the compliment, {Gender()}"
                print(a)
                speak(a)

            elif 'stop listening' in query or 'exit program' in query or 'off' in query or 'close program' in query or 'get lost' in query:
               speak(f"Ok {Gender()}, Have a nice day! if any assistance you need, Please ask")
               callAssistant(b)   
            
            elif f'hold on {Name()}' in query or f'go to sleep' in query:
               Sleep(query)
               


if __name__=="__main__":
    
    
    b=0
    callAssistant(b) 
  
