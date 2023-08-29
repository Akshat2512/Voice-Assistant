
import datetime
import os
import random
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia

from gen_test import record_to_file, extract_feature
from utils import create_model
    
model = create_model()
model.load_weights("Python Projects/voiceassistant/model.h5")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[-1].id)
engine.setProperty('rate',150) 

def speak(audio):
   
   engine.say(audio)
   engine.runAndWait()


def Gender():
    file='Python Projects/voiceassistant/recorded.wav'
    features = extract_feature(file, mel=True).reshape(1, -1)
       
    male_prob = model.predict(features)[0][0]
    female_prob = 1 - male_prob
      
    if male_prob > female_prob:
       return "Sir" 
    else :
        return "Mam"
    
    
def Name():
    a='Cortana'
    return a
   

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
     a=random.randint(0,1)
     if a==0 :
      speak(f"Ok {Gender()}, Going to sleep....")
     elif a==1 :
      speak(f"Ok {Gender()}, Leaving out....")      
     elif a==1 :
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




def Music(query,dir):
  print(query,dir)
  def fav():
        dir = 'C:\\\\Users\\\\Akshat\\\\Music\\\\My Songs' 
        a="01" 
        file1=open("C:\\Users\\Akshat\\Documents\\C C++\\Memory.txt","w") 
        file1.write(a)
        file1.close()
        return dir

  def ran(): 
        dir = 'C:\\\\Users\\\\Akshat\\\\Music\\\\Songs'
        a="10"
        file1=open("C:\\Users\\Akshat\\Documents\\C C++\\Memory.txt","w") 
        file1.write(a)
        file1.close()
        print(len(dir))
        return dir
                
  b=1 
  while True:
    
      songs = os.listdir(dir) 
      print(songs)
        
      i=0    
      while i<len(songs):
          
        if f'{query}' in songs[i].lower():
          os.startfile(os.path.join(dir, songs[i]))
          
        elif 'my songs' in query:
          print("Directing to New playlist....")
          dir=f'{fav()}'

          break
        elif 'all' in query or 'every' in query or 'just play' in query or 'any' in query or 'wish' in query:
          print("Changing the directory of playlist...")
          dir=f'{ran()}'
          if 'you play' in query: 
           query='next' 
          break
        elif 'let me' in query or 'myself' in query or 'control' in query:
             try:
              os.kill('TASKKILL /F /IM python.exe') 
        
             except Exception as e:
                return "None"
             break
        elif 'stop playing' in query:
               try:
                os.system('TASKKILL /F /IM Music.UI.exe') 
                
               except Exception as e:
                 return "None"
              
             

        elif 'next' in query: 
          songs=os.listdir(dir)
          n=random.randint(0,len(songs)-1)
          print(len(songs))
          print (n)
          os.startfile(os.path.join(dir,songs[n]))
          query=takeCommand(b).lower()
          if 'you do this' in query:
            Music(query,dir)
          Music(query,dir) 
        
        elif 'you do this' in query or 'you play' in query: 
                
                file1= open("C:\\Users\\Akshat\\Documents\\C C++\\Python Projects\\Play.py","r")
                data=file1.readlines()
                data[3]=f"dir= '{dir}'\n"
                file1= open("C:\\Users\\Akshat\\Documents\\C C++\\Python Projects\\Play.py","w")
                file1.writelines(data)
                file1.close()
               
                os.startfile(os.path.join("C:\\Users\\Akshat\\Documents\\C C++\\Python Projects\\Play.py"))
                pid=os.getpid()
      
                print("Process ID:",pid)
                
                
                # output = os.popen('wmic process get description, processid').readlines()
                # if os.popen('wmic process get description') == "python":
                #   print(output)
                query=takeCommand(b).lower()
                if 'let me' in f'{query}':
                  
                  Music(query,dir)
                Music(query,dir)
                
               
        elif 'close music' in query or 'stop playing music' in query or 'turn off music' in query:
                a="Quitting Playing Music?"
                print(a)
                speak(a)
                os.system('TASKKILL /F /IM Music.UI.exe') 
                b=0      
                   
        elif 'get back' in query:
            main()
  
        i=i+1
      print("choose the song...")
      query=takeCommand(b).lower()

def Calculate(query):

  k=query.split(" ")

  j=0
  a=[]
  b=[]


  while j<len(k):
    
   if 'multi' in k[j].lower() or 'div' in k[j].lower() or  'add' in k[j].lower() or  'sub' in k[j].lower() or  'square' in k[j].lower(): 
    a.append(k[j])
   if k[j]. isdigit():
    a.append(k[j])
   j=j+1
  print (a)


  j=0
  if a[0]. isdigit():
   c=a[0]
  else: 
   c='1'
 
  while j<len(a):
    if 'multi' in a[j].lower():
        i=j+1
        while i<len(a):
         
         if 'multi' in a[i].lower() or 'div' in a[i].lower() or  'add' in a[i].lower() or  'sub' in a[i].lower() or  'square' in a[i].lower():
            break
         elif a[i].isdigit():
          c=c+'*'+a[i]
         i=i+1 
    elif 'div' in a[j].lower():
        i=j+1
        while i<len(a):
         if 'multi' in a[i].lower() or 'div' in a[i].lower() or  'add' in a[i].lower() or  'sub' in a[i].lower() or  'square' in a[i].lower():
            break
         elif a[i].isdigit():
          c=c+'/'+a[i]   
         i=i+1 
    elif 'sub' in a[j].lower():
        i=j+1
        c=0
        while i<len(a):
        
         if 'multi' in a[i].lower() or 'div' in a[i].lower() or  'add' in a[i].lower() or  'sub' in a[i].lower() or  'square' in a[i].lower():
            break
         c=a[i]+'-'+a[i+1]
         i=i+1 
    elif 'add' in a[j].lower():
        i=j+1
        while i<len(a):
        
         if 'multi' in a[i].lower() or 'div' in a[i].lower() or  'add' in a[i].lower() or  'sub' in a[i].lower() or  'square' in a[i].lower():
            break
         c=c+'+'+a[i]    
         i=i+1 
                  
    j=j+1

  print(c)
  d=eval(c)
  print(d)
  speak(d)

    

def takeCommand(b=0):
    #It takes microphone input from the user and returns string output
    file=''
    query=''
    if not file or not os.path.isfile(file):
            print("Listening...")
            file='recorded.wav'

            record_to_file(file)
                    

    r = sr.Recognizer()
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

    strTime = datetime.datetime.now().strftime("%M:%S")
    a=f"{hour}:{strTime}, {day}"    
    print(a)
    return a

def Date_Time(query):
    a=" " 
    if 'the year' in query:
     a=datetime.datetime.now().strftime("%Y")
    elif 'the day' in query or 'is week' in query:
     a=datetime.datetime.now().strftime("Today is %D and week is %A")
    elif 'the month' in query:
     a=datetime.datetime.now().strftime("%B")
    elif 'the date' in query:
     a=datetime.datetime.now().strftime("Today's date is %d:%B:%Y, %A")  
    elif 'the time' in query:
       a=Time()
       
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
                    print(results)
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
            
                    
            elif 'play' in query or 'play song' in query:
                   
                    
                    file1=open("C:\\Users\\Akshat\\Documents\\C C++\\Memory.txt","r")
                    
                    a=file1.read(1)
                    music_dir = 'C:\\\\Users\\\\Akshat\\\\Music\\\\Songs'
                    songs=os.listdir(music_dir)
                    dir=', '.join(songs)
                    print(dir)
                    if '1' in a or ' ' in a:
                            
                             
                            while(True):
                                c=f"{Gender()}, Which song you wants to play?"
                                print(c)
                                speak(c)
                                query = takeCommand(b).lower()
                                if f'{query}' in dir.lower() or 'let me' in query or 'myself' in query or'you choose' in query or 'you do this' in query or 'you play' in query:
                                 Music(query,music_dir)
                                
                                elif 'sorry' in query or 'leave it' in query or 'exit' in query:
                                    speak(f"Ok {Gender()}, Cancelling Playing Music....")
                                    a="10"
                                    main()
                                
                                else:
                                    a="10"
                                    n=random.randint(0,3)
                                    if n==0:
                                     speak(f"My apologies {Gender()}, I am not quite sure how to respond to that. ")
                                    elif n==1:
                                     speak(f"Sorry {Gender()}! You are not audible")
                                    elif n==2:
                                      speak(f"Sorry {Gender()}! I think my earpiece is not working properly. Could You please repeat?")      
                                    elif n==3:
                                      speak(f"My apologies {Gender()}! I didn't get that")   
                    
                    elif '0' in a: 
                        speak(f"{Gender()}, Could I play your last playlist?")   
                        query = takeCommand(b).lower()   
                        if 'yes' in query or 'go ahead' in query or 'go head' in query or 'go on' in query or 'keep up' in query:
                            query='you choose'
                            music_dir = 'C:\\\\Users\\\\Akshat\\\\Music\\\\My Songs' 
                            speak(f"Ok {Gender()}!")
                            a="01" 
                            file1=open("Memory.txt","w") 
                            file1.write(a)
                            file1.close()
                            Music(query,music_dir)
                            
                        
                        elif 'no' in query or 'let me choose' in query: 
                            music_dir = 'C:\\\\Users\\\\Akshat\\\\Music\\\\Songs'
                            speak(f"Ok {Gender()}!")
                            a="10" 
                            file1=open("Memory.txt","w") 
                            file1.write(a)
                            file1.close()
                            Music(query,music_dir)
                    
             

            elif 'close music' in query or 'stop playing music' in query or 'turn off music' in query:
                os.system('TASKKILL /F /IM Music.UI.exe') 
                b=0      
                       
            elif 'close browser' in query or 'stop browser' in query or 'turn off browser' in query:
                 os.system("TASKKILL /F /IM msedge.exe")
                     
                 
            elif 'time' in query or 'the date' in query or 'the day' in query or 'the year' in query or'the month' in query:
                a=Date_Time(query)
                print(a)
                speak(a)

            elif 'nice' in query or 'well done' in query or 'good job' in query or 'Excellent Work' in query:
                a=f"Thanks for the compliment, {Gender()}"
                print(a)
                speak(a)

            elif 'stop listening' in query or 'exit program' in query or 'off' in query or 'close program' in query or 'get lost' in query:
               speak(f"Ok {Gender()}, Have a nice day! if any assistance you need, Please ask")
               callAssistant(b)

            elif 'multi' in query or 'div' in query or  'add' in query or  'sub' in query or  'square' in query or 'solve' in query or 'calculate' in query:
                 
                 b=0
                 if 'solve' in query or 'calculate' in query:
                   speak("What do you want to calculate?")
                   query=takeCommand(b).lower()
                 
                 else:
                   Calculate(query) 
                 Calculate(query)     
            
            elif f'hold on {Name()}' in query or f'go to sleep' in query:
               Sleep(query)
               


if __name__=="__main__":
    
    
    b=0
    callAssistant(b) 
  
