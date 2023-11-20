import pyttsx3
import speech_recognition as sr
import datetime
import time
import wikipedia
import webbrowser
import os
import sys
import pywhatkit
import requests
import matplotlib.pyplot as plt
import numpy as np
import PyPDF2
import plyer
import pyautogui
import speedtest
import random
import pyperclip
from pywikihow import search_wikihow
from bs4 import BeautifulSoup 
from plyer import notification
from pytube import YouTube
from pytube import Playlist
from moviepy.editor import *
from gtts import gTTS
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
engine=pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
engine.setProperty('rate',150)
def speak(audio):
    engine.say(audio)
    engine.runAndWait() 
def takeCommand():
   r=sr.Recognizer()
   with sr.Microphone() as source:
      print("listening....")
      r.pause_threshold=1
      audio=r.listen(source)
   try:
      print("Recognizing...")
      query = r.recognize_google(audio,language='en-in')
      print(f"user said : {query}")
   except Exception as e:
      print("Say that again please...")
      return "None"
   return query
def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="city_distance_calculator")
    location = geolocator.geocode(city_name)
    if location:
        return location.latitude, location.longitude
    else:
        return None
def calculate_distance(city1, city2):
    coords1 = get_coordinates(city1)
    coords2 = get_coordinates(city2)
    if coords1 and coords2:
        return geodesic(coords1, coords2).kilometers
    else:
        return None
def fetch_random_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    data = response.json()
    joke = data.get("joke") or (data.get("setup") + " " + data.get("delivery"))
    return joke
def alarm(query):
    timehere = open("Alarmtxt.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarmtxt.py")
def video_music():
    play="C:\\Users\\HARSHIT BHATT\\Desktop\\code\\jrvis\\playlist\\vdo"
    while True:
        songs = os.listdir(play)
        numberr=random.randint(1,78)
        os.startfile(os.path.join(play, songs[numberr]))
        speak("do you wants to play next song")
        query=takeCommand().lower()
        if "yes play next song" in query:
            speak("sure sir happy to hear")
            continue
        elif "no" in query:
            speak("thankyou for using our music player")
            break
def old_Audio_music():
    play="C:\\Users\\HARSHIT BHATT\\Desktop\\code\\jrvis\\playlist\\oldaud"
    while True:
        songs = os.listdir(play)
        numberr=random.randint(1,30)
        os.startfile(os.path.join(play, songs[numberr]))
        speak("do you want to play next song")
        query=takeCommand().lower()
        if "yes" in query:
            speak("sure sir happy to hear")
            continue
        elif "no" in query:
            speak("thankyou for using our music player")
def new_audio_music():
    play="C:\\Users\\HARSHIT BHATT\\Desktop\\code\\jrvis\\playlist\\newaud"
    while True:
        songs = os.listdir(play)
        numberr=random.randint(1,114)
        os.startfile(os.path.join(play, songs[0]))
        speak("do you want to play next song")
        query=takeCommand().lower()
        if "yes" in query:
            speak("sure sir happy to hear")
            continue
        elif "no" in query:
            speak("thankyou for using our music player")
            break            
def get_random_fact_from_internet():
    try:
        url = "https://uselessfacts.jsph.pl/random.json?language=en"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data["text"]
        else:
            return "Unable to fetch a random fact at the moment."
    except Exception as e:
        return f"An error occurred: {str(e)}" 
def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Harshit sir The time is {strTime}")
    search="temperature in dehradun"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div",class_="BNeawe").text
    speak(f"current {search} is {temp}")
    speak("I am Jarvis sir Please tell me how may I help you") 
if __name__=="__main__":
    # WishMe()
    # root=Tk()
    # root.configure(background='black')
    # bg=PhotoImage(file='js.gif')
    # Bgpic=Label(root,image=bg)
    # Bgpic.place(x=0,y=0)
    # greet = Label(root, text="JARVIS AI",font=("ALGERIAN",80),foreground='dark blue',background='black')
    # greet.pack()
    # vc = Button(root, text="Speak",command=WishMe)
    # vc.place(x=100,y=400)
    # root.mainloop()
    while True:    
        query = takeCommand().lower()
        if 'wikipedia' in query:
           speak('Searching Wikipedia...')
           query=query.replace('wikipedia', "")
           results=wikipedia.summary(query, sentences=2)
           speak("According to wikipedia")
           print(results)
           speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
        elif 'open zee5' in query:
            webbrowser.open("https://www.zee5.com")
        elif 'open sonyliv' in query:
            webbrowser.open("https://www.sonyliv.com") 
        elif 'open stackoverflow' in query:
            webbrowser.open("https://www.stackoverflow.com")  
        elif 'open vs code' in query:
            codePath = "C:\\Users\\HARSHIT BHATT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)     
        elif 'erp' in query:
            if 'hill' in query:
                webbrowser.open("https://erp.gehu.ac.in")  
            elif 'deemed' in query:
                webbrowser.open("https://erp.geu.ac.in")
        elif "history" in query:
            pyautogui.hotkey("ctrl","h")
        elif "trash history" in query:              
            pyautogui.hotkey("ctrl","h")
            pyautogui.hotkey("ctrl","a")
            pyautogui.press("delete")
            pyautogui.press("enter")   
        elif 'time' in query or 'current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'who are you' in query:
            speak("I am your friend and your voice assistant")
        elif 'who is your creator' in query:
            speak("My creator is Harshit Bhatt.")
        elif 'play some cultural songs' in query:
            webbrowser.open("https://www.youtube.com/watch?v=0ea9z7bQAe8&list=RDMM0ea9z7bQAe8&start_radio=1")
        elif 'what is the name of my pet' in query:
            speak("hello sir your pet name is Jimmy")      
        elif 'google search' in query:
            import wikipedia as googlescrap
            query = query.replace("jarvis","")
            query = query.replace("google search for","")
            query= query.replace("google","")
            speak("thats what i found on web!")
            try:
                pywhatkit.search(query)
                result = googlescrap.summary(query,3)
                speak(result)
            except:
                speak("no speakable data Avilable!")    
        elif 'search youtube' in query or 'search in youtube' in query:
            speak("this is what i found for your search!")
            query = query.replace("youtube search for", "")
            query= query.replace("in youtube", "")
            query = query.replace("jarvis", "")
            query=query.replace("search ","")
            query=query.replace("on","")
            query=query.replace("for","")
            query=query.replace("youtube","")
            web =  "https://www.youtube.com/results?search_query=" + query 
            webbrowser.open(web)
            pywhatkit.playonyt(query)
            speak("done sir")
        elif "schedule my day" in query:                            
            tasks= [] 
            speak("do you want to clear your all old tasks, please say yes delete data, if you want")
            query=takeCommand().lower()
            if 'delete' in query:
                file=open("tasks.txt","w")
                file.write(f"")
                file.close()
                print("Your task is complete")
            no_tasks=int(input("enter the no of tasks :- "))
            i = 0
            for i in range(no_tasks):
                tasks.append(input("enter the tasks :- "))
                file=open("tasks.txt","a")
                file.write(f"{i+1}. {tasks[i]}\n")
                file.close()
        elif "my schedule" in query:
            file = open("tasks.txt","r")
            content = file.read()
            file.close()
            notification.notify(
                title = "my schedule :-",
                message = content,
                timeout = 15
            ) 
        elif "temperature in" in query:
            url = f"https://www.google.com/search?q={query}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {query} is {temp}")
        elif 'open python' in query:
            pathcoder="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.11\\IDLE (Python 3.11 64-bit).lnk"
            os.startfile(pathcoder)
        elif "in calculator" in query: #change the code
            if "addition" in query:
                audio=speak("please speak first number")
                a=takeCommand()
                audio=speak("please speak second number")
                b=takeCommand()
                y=int(a)+int(b)
                speak(y)
            elif "subtraction" in query:
                audio=speak("please speak first number")
                a=takeCommand(audio)
                audio=speak("please speak second number")
                b=takeCommand(audio)
                if int(a)<int(b):
                    x=int(a)-int(b)
                    speak(x)
                elif int(b)<int(a):
                    x=int(b)+int(a)
                    speak(x)
            elif "multiplication" in query:
                audio=speak("please speak first number")
                a=takeCommand(audio)
                audio=speak("please speak second number")
                b=takeCommand(audio)
                x=int(a)*int(b)
                speak(x)
            elif "division" in query:
                audio=speak("please speak first number")
                a=takeCommand(audio)
                audio=speak("please speak second number")
                b=takeCommand(audio)
                x=int(a)/int(b)
                speak(x)
        elif 'activate how to do mode' in query:
            speak("How to do mode is activated")
            while True:
                speak("please tell me what you want")
                how = takeCommand()
                try:
                    if "exit" in how or "close" in how:
                        speak("okey sir,how to do mode is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to)==1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e :
                    speak("sorry sir,i am not able to find this")
        elif 'how much battery left' in query or "how much power is left" in query or 'battery' in query:
            import psutil
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery")    
        elif 'hard disk' in query or 'hard disc' in query:
            pathcode= "C:\\Users\\HARSHIT BHATT\\Desktop\\code\\jrvis\\This PC - Shortcut.lnk"
            os.startfile(pathcode)     
        elif 'play video' in query:
            pyautogui.press("k")
            speak("video played")
        elif 'next video' in query:
            pyautogui.press("j")
            speak("next video played")
        elif 'previous video' in query:
            pyautogui.press("k")
            speak("previous video played")
        elif 'mute' in query:
            pyautogui.press("m")
            speak("video muted")
        elif 'unmute' in query:
            pyautogui.press("m")
            speak("video unmuted")    
        elif 'volume up' in query: #check it
            from keyboard import volumeup
            speak("turning volume up sir")
            volumeup()
        elif 'volume down' in query: #check it
            from keyboard import volumedown
            speak("turning  volume down")
            volumedown()
        elif "shutdown system" in query:
             speak("are you sure you wants to shutdown")   
             shutdown = input("do you want to shutdown your system(yes/no)")
             if shutdown == 'yes':
                os.system("shutdown /s /t 1")
             elif shutdown == 'no':
                continue
        elif "quit" in query:
            speak("thankyou sir for using me see you next time!")
            break      
        elif 'pause video' in query:
            pyautogui.press("space")
            speak("video paused")      
        elif 'search in web' in query or 'search web' in query:
           query=query.replace("search","") 
           query=query.replace("web","")
           query=query.replace("on", "")
           code=(f"https://www.{query}")
           webbrowser.open(code)
        elif "skip video back" in query:
            pyautogui.press("j")
        elif "forward" in query:
            pyautogui.press("l") 
        elif "full screen" in query:
            pyautogui.press("f")  
        elif "internet speed" in query or 'speed test' in query:
            speak("sir speed test is in progress, please wait for a minute to see the results")
            wifi = speedtest.Speedtest()
            upload_net=wifi.upload()/1048576
            download_net=wifi.download()/1048576
            print("Wifi download speed is",round(download_net/8,2),"MB")
            print("Wifi upload speed is",round(upload_net/8,2), "MB")
            speak(f"wifi download speed is {round(download_net/8,2)} MegaByte")
            speak(f"wifi upload speed is {round(upload_net/8,2)} MegaByte")
        elif  'play next song' in query:
            pyautogui.press("j")
            speak("the next song played")
        elif "play previous song" in query:
            pyautogui.press("k")
            speak("the previous song played")
        elif "play current song" in query:
            pyautogui("l")
            speak("the song has played")
        elif "play music" in query:
            speak("would you like to play music online or offline")
            query=takeCommand().lower()
            if "offline" in query:  
                speak("what kind of music you want me to play ")
                speak("video or audio")
                query=takeCommand().lower()
                if "audio" in query:
                    speak("Would you like to play old audio or new audio")
                    query=takeCommand().lower()
                    if "old audio" in query:
                        old_Audio_music()
                    elif "new audio" in query:
                        new_audio_music()
                elif "video" in query:
                    video_music()
                else:
                    speak("your section is invalid")
                    continue
            elif "online" in query:
                speak("which song would you like to play")
                query=takeCommand().lower()
                speak("this is what i found on youtube music!")
                query=query.replace("play music","")
                query=query.replace("jarvis", "")
                uery=query.replace("music","")
                webt = "https://music.youtube.com/search?q=" + query
                webbrowser.open(webt)
                pywhatkit.playonyt(query)
                speak("done sir!")
        elif "download current video" in query:
            pyautogui.hotkey("Ctrl","l")
            pyautogui.hotkey("Ctrl","c")
            pyautogui.hotkey("Ctrl","v")
            data=pyperclip.paste()
            video_link=data
            print("video downloading....")
            speak("video started downloading")
            YouTube(video_link).streams.get_highest_resolution().download("C:\\Users\\HARSHIT BHATT\\Desktop\\code\\jrvis\\playlist")
            print("video downloaded successfully")
            speak("video downloaded successfully")
        elif "download current song" in query:
            pyautogui.hotkey("Ctrl","l")
            pyautogui.hotkey("Ctrl","c")
            pyautogui.hotkey("ctrl","v")
            data=pyperclip.paste()
            video_link=data
            link=video_link
            youtube_1=YouTube(link)
            videos=youtube_1.streams.filter(only_audio=True)
            vid = list(enumerate(videos))
            for i in vid:
                print(i)
            print()
            inp=4
            speak("the current song is started downloading")
            videos[inp].download("C:\\Users\\HARSHIT BHATT\\Desktop\\code\\jrvis\\playlist")
            print("successfully")
            speak("the current song is downloaded successfully")
        elif "download current movie " in query:
            pyautogui.hotkey("Ctrl","l")
            pyautogui.hotkey("Ctrl","c")
            pyautogui.hotkey("ctrl","v")
            data=pyperclip.paste()
            video_link=data
            print("video downloading....")
            speak("video downloading started")
            YouTube(video_link).streams.get_highest_resolution().download("C:\\Users\\HARSHIT BHATT\\Desktop\\code\\jrvis\\playlist")
            print("video downloaded successfully...")
            speak("the current movie is downloaded successfully")
        elif "close " in query:
            pyautogui.hotkey("alt","f4") 
        elif "who is my best friend" in query:
            speak("Akshay Kumar is your best friend sir")     
        elif "download current playlist" in query:
            pyautogui.hotkey("Ctrl","l")
            pyautogui.hotkey("Ctrl","c")
            pyautogui.hotkey("ctrl","v")
            data=pyperclip.paste()  
            link=data            
            yt_playlist=Playlist(link)
            speak("the current video downloading started")
            for video in yt_playlist.videos: 
               video.streams.get_highest_resolution().download("C:\\Users\\HARSHIT BHATT\\Desktop\\code\\jrvis\\playlist")
               print("video downloaded :",video.title)
            print("\nall videos are downloaded")
            speak("the current playlist is downloaded successsfully") 
        elif "increase brightness" in query:
            pyautogui.press("F12")
        elif "decrease brightness" in query:
            pyautogui.press("F11")
        elif "screen capture" in query:
            pyautogui.hotkey("windows","alt","PrtSc")   
        elif "download audio playlist" in query:
            pyautogui.hotkey("Ctrl","l")
            pyautogui.hotkey("Ctrl","c")
            pyautogui.hotkey("ctrl","v")
            data=pyperclip.paste()
            print("audio songs started downloading")
            speak("audio songs is started downloading")
            playlist_url = data
            playlist = Playlist(playlist_url)
            for video in playlist.videos:
                 audio_stream = video.streams.filter(only_audio=True).first()
                 audio_stream.download(output_path="C:\\Users\\yashm\\Desktop\\playlist\\rahni2")
            print("audio songs downloaded successfully")
            speak("the audio playlist is downloaded successfully")    
        elif "read pdf now" in query:
            book=open("C:\\Users\\HARSHIT BHATT\\Desktop\\code\\jrvis\\readpdf\\dsa.pdf","rb")
            pdfReader=PyPDF2.PdfReader(book)
            speaker = pyttsx3.init()
            speak("do you wants to read whole pdf or single pdf page")
            query=takeCommand().lower()
            if "hole" in query:
                pages=len(pdfReader.pages)
                for i in range(1,pages):
                    pages= pdfReader.pages[i]
                    text=pages.extract_text()
                    speaker.say(text)
                    speaker.runAndWait()
                speak("thanks for using our pdf reader")
                speak("have a good day!")
            elif "single page" in query:
                book=open("C:\\Users\\HARSHIT BHATT\\Desktop\\code\\jrvis\\readpdf\\dsa.pdf","rb")
                pdfReader=PyPDF2.PdfReader(book)
                speaker = pyttsx3.init()
                x=int(input("which pages you wants me to read : "))
                pages= pdfReader.pages[x-1]
                text=pages.extract_text()
                speaker.say(text)
                speaker.runAndWait()
                speak("do you wants to continue reading")
                take=takeCommand().lower()
                if "yes" in take:
                    continue 
                else:
                    speak("thanks for using our pdf reader")
                    speak("have a good day!")
        elif "space news" in query:
            api_key="IWpUHBu2WtSbYliWg39tmfUoppUxPwJg0iXbkvFp"
            speak("please enter the date")
            x=input("enter the date in YYYY-MM-DD format ")    
            def nasaNews(date):
              speak("extracting the data from nasa")
              url = "https://api.nasa.gov/planetary/apod?api_key="+str(api_key)
              Params={'date':str(date)}
              r=requests.get(url,params=Params)
              data=r.json()
              print(data)
              info=data['explanation']
              Title=data['title']
              print(info)
              speak(f"Title :{Title}")    
              speak(f"According to nasa :{info}")
            nasaNews(x)
        elif "tell headlines" in query:
            api_key="c0f723e3ecf348aa8fedfb0d0a91db75"
            def news(): 
                main_url="https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey="+api_key
                news=requests.get(main_url).json()
                article=news["articles"]
                news_article=[]
                for arti in article:
                    news_article.append(arti['title'])
                for i in range(len(news_article)):
                    print(news_article[i])
                    speak(news_article[i])

            news()
        elif "tell me a joke" in query:
            joke = fetch_random_joke()
            if joke:
                print("Here's a joke for you:")
                print(joke)
                speak(joke)
            else:
                print("Sorry, I couldn't fetch a joke this time.")
        elif "tell me a fact" in query:
                random_fact = get_random_fact_from_internet()
                print("Random Fact:", random_fact)
                speak(random_fact)
        elif "distance" in query:
               city1 = input("Enter the name of the first city: ")
               city2 = input("Enter the name of the second city: ")

               distance = calculate_distance(city1, city2)
               if distance is not None:
                    print(f"The distance between {city1} and {city2} is {distance:.2f} kilometers by air.")
                    speak(f"The distance between {city1} and {city2} is {distance:.2f} kilometers by air")
               else:
                    print("One or both city names could not be found.")
                    speak("One or both city names could not be found")
        elif "mp3" in query or "convert to mp3" in query:
            input_directory = "C:\\Users\\HARSHIT BHATT\\Desktop\\code\\jrvis\\playlist"
            output_directory ="C:\\Users\\HARSHIT BHATT\\Desktop\\code\\jrvis\\playlist"
            for filename in os.listdir(input_directory):
                if filename.endswith(".mp4"):
                    video = VideoFileClip(os.path.join(input_directory, filename))
                    mp3_filename = os.path.splitext(filename)[0] + ".mp3"
                    video.audio.write_audiofile(os.path.join(output_directory, mp3_filename))
            print("Conversion completed.")
    
