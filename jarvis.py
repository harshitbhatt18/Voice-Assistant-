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
from bs4 import BeautifulSoup 
from plyer import notification
import matplotlib.pyplot as plt
import numpy as np
from pywikihow import search_wikihow
import PyPDF2
import plyer
import pyautogui
import speedtest
import random
import pyperclip
from pytube import YouTube
from pytube import Playlist
from moviepy.editor import *
from gtts import gTTS
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import PyPDF2
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
def alarm(query):
    timehere = open("Alarmtxt.txt","a")#check it
    timehere.write(query)
    timehere.close()
    os.startfile("alarmtxt.py")
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
        # numberr=random.randint(1,523)
        os.startfile(os.path.join(play, songs[1]))
        speak("do you wants to play next song")
        query=takeCommand().lower()
        if "why" in query:
            speak("sure sir happy to hear")
            continue
        elif "no" in query:
            speak("thankyou for using our music player")
            break
def old_Audio_music():
    play="C:\\Users\\HARSHIT BHATT\\Desktop\\code\\jrvis\\playlist\\oldaud"
    while True:
        songs = os.listdir(play)
        # numberr=random.randint(1,800)
        os.startfile(os.path.join(play, songs[0]))
        speak("do you want to play next song")
        query=takeCommand().lower()
        if"why" in query:
            speak("sure sir happy to hear")
            continue
        elif "no" in query:
            speak("thankyou for using our music player")
def new_audio_music():
    play="C:\\Users\\HARSHIT BHATT\\Desktop\\code\\jrvis\\playlist\\newaud"
    while True:
        songs = os.listdir(play)
        # numberr=random.randint(1,70)
        os.startfile(os.path.join(play, songs[0]))
        speak("do you wants to play next song")
        query=takeCommand().lower()
        if "why" in query:
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
        elif 'open erp' in query:
            if 'hill' in query:
                webbrowser.open("https://erp.gehu.ac.in")  
            elif 'deemed' in query:
                webbrowser.open("https://erp.geu.ac.in")
        elif "history" in query:
            pyautogui.hotkey("ctrl","h")
        elif "hand" in query:
            text="""In this example, we first import the pywhatkit library, which includes the text_to_handwriting() function 
            for handwriting synthesis. We then use the clipboard module of the library to get the text that has been copied to the clipboard, 
            and store it in the text variable. Finally, we pass the text variable to the text_to_handwriting() function, which generates a 
            handwritten image of the text and saves it to a file named "handwritten.png" in the current directory.
            Note that the text_to_handwriting() function uses a default font and style for the handwriting, but you can customize these by passing additional arguments to the function. 
            Additionally, the pywhatkit library requires the installation of the pyautogui and pillow packages, which you can install using pip."""
            pywhatkit.text_to_handwriting(text,"demo1.png",[0,0,138])    
        elif "trash history" in query:               #check this
            pyautogui.hotkey("ctrl","h")
            pyautogui.hotkey("ctrl","a")
            pyautogui.press("delete")
            pyautogui.press("enter")   
        elif 'weather today' in query:    
            webbrowser.open("https://www.google.com/search?q=weather&rlz=1C1VDKB_enIN1025IN1025&oq=whe&aqs=chrome.1.69i57j0i10i131i433i512j0i512l4j0i10i433i512j0i10i433i457i512j0i402l2.3410j0j15&sourceid=chrome&ie=UTF-8")      
        elif 'time right now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir The time is {strTime}")
        elif 'who are you' in query:
            speak("I am your friend and your voice assistence")  
        elif 'play a song' in query:
            webbrowser.open("https://www.youtube.com/watch?v=cZSrWoBMSrg")
        elif 'play a movie' in query:
            webbrowser.open("https://www.youtube.com/watch?v=B6h-kQLQqec")
        elif 'i left' in query:                                             #check it
            webbrowser.open("https://www.youtube.com/watch?v=MoeQlmeJnPg&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=3")
        elif 'open vs code' in query:
            codePath = "C:\\Users\\HARSHIT BHATT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open chrome' in query:
            codePAth="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePAth)
        elif 'open youtube for harshit' in query:
            codePaTh="C:\\Users\\HARSHIT BHATT\\Desktop\\code\\jrvis\\YouTube.lnk"
            os.startfile(codePaTh)
        elif 'open email for harshit' in query:
            CodePath="C:\\Users\\HARSHIT BHATT\\Desktop\\code\\jrvis\\Gmail.lnk"
            os.startfile(CodePath)
        elif 'who is your creator' in query:
            speak("My creators are Akshay Kumar and Harshit Bhatt.")
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
        elif 'search youtube' in query:
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
        elif 'play music' in query:
            speak("this is what i found on youtube music!")
            query=query.replace("play music","")
            query=query.replace("jarvis", "")
            uery=query.replace("music","")
            webt = "https://music.youtube.com/search?q=" + query
            webbrowser.open(webt)
            pywhatkit.playonyt(query)
            speak("done sir!")
        elif "schedule my day" in query:                            
            tasks= [] 
            speak("do you want to clear your all old tasks")
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
        elif "in calculator" in query:
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
        elif "open" in query:
            query=query.replace("open","")
            query=query.replace("jarvis","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.press('enter')
            pyautogui.press('enter')        
        elif 'play video' in query:
            pyautogui.press("k")
            speak("video played")
        elif 'mute' in query:
            pyautogui.press("m")
            speak("video muted")
        elif 'unmute' in query:
            pyautogui.press("m")
            speak("video unmuted")    
        elif 'volume up' in query:
            from keyboard import volumeup
            speak("turning volume up sir")
            volumeup()
        elif 'volume down' in query:
            from keyboard import volumedown
            speak("turning  volume down")
            volumedown()
        elif "shutdown system" in query:
             speak("are you sure you wants to shutdown")   
             shutdown = input("do you want to shutdown your system(yes/no)")
             if shutdown == 'yes':
                os.system("shutdown /s /t 1")
             elif shutdown == 'no':
                break
        elif "you can take a break" in query:
            speak("thankyou sir for using me see you next time!")
            speak("just say wake up jarvis!")
            break      
        elif 'space video' in query:
            pyautogui.press("space")
            speak("video paused")      
        elif "restart system" in query:
             speak("are you sure you wants to restart")   
             shutdown = input("do you want to restart your system")
             if shutdown == 'yes':
                os.system("restart /s /t 1")
             elif shutdown == 'no':
                break            
        elif 'search on web' in query:
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
        elif "loafer" in query:
            play="C:\\Users\\yashm\\Desktop\\playlist\\lofi"
            songs = os.listdir(play)
            numberr=random.randint(1,116)
            os.startfile(os.path.join(play, songs[numberr]))                         
        elif "popular song" in query:
            webbrowser.open("https://www.youtube.com/watch?v=iHdYhdDg1Co")   
        elif "set an alarm" in query:
            print("input time example : 10 and 10 and 10")
            speak("set the time")
            a = input("please tell the time :-")
            alarm(a)
            speak("done,sir")
        elif "internet speed" in query:
            wifi = speedtest.Speedtest()
            upload_net=wifi.upload()/1048576
            download_net=wifi.download()/1048576
            print("Wifi download speed is",round(download_net/8,2),"MB")
            print("Wifi upload speed is",round(upload_net/8,2), "MB")
            speak(f"wifi download speed is {round(upload_net/8,2)} MB")
            speak(f"wifi upload speed is {round(upload_net/8,2)} MB")
        elif  'play next song' in query:
            pyautogui.press("j")
            speak("the next song played")
        elif "play previous song" in query:
            pyautogui.press("k")
            speak("the previous song played00")
        elif "play current song" in query:
            pyautogui("l")
            speak("the song has played")
        elif "music" in query:
            speak("what kind of music you wants me to play ")
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
                break
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
            YouTube(video_link).streams.get_highest_resolution().download("C:\\Users\\yashm\\Desktop\\playlist")
            print("video downloaded successfully...")
            speak("the current movie is downloaded successfully")
        elif "download current full playlist" in query:
            pyautogui.hotkey("Ctrl","l")
            pyautogui.hotkey("Ctrl","c")
            pyautogui.hotkey("ctrl","v")
            data=pyperclip.paste()
            link=data
            yt_playlist=Playlist(link)
            speak("the current video downloading started")
            for video in yt_playlist.videos: 
               video.streams.get_highest_resolution(1).download("C:\\Users\\yashm\\Desktop\\c+")
            print("video downloaded :",video.title)
            print("\nall videos are downloaded")
            speak("the current playlist is downloaded successsfully")
        elif "close " in query:
            pyautogui.hotkey("alt","f4")    
        elif "download current punjabi playlist" in query:
            pyautogui.hotkey("Ctrl","l")
            pyautogui.hotkey("Ctrl","c")
            pyautogui.hotkey("ctrl","v")
            data=pyperclip.paste()
            link=data
            yt_playlist=Playlist(link)
            speak("the current video downloading started")
            for video in yt_playlist.videos: 
               video.streams.get_highest_resolution().download("C:\\Users\\yashm\\Desktop\\playlist\\punjabi songs best")
            print("video downloaded :",video.title)
            print("\nall videos are downloaded")
            speak("the current playlist is downloaded successfully")
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
               video.streams.get_highest_resolution().download("C:\\Users\\yashm\\Desktop\\playlist\\logic")
               print("video downloaded :",video.title)
            print("\nall videos are downloaded")
            speak("the current playlist is downloaded successsfully") 
        elif "restart laptop" in query:
            pyautogui.hotkey("alt","f4")
            pyautogui.hotkey("alt","f4")
            pyautogui.hotkey("pageDown")
            pyautogui.hotkey("enter")
            speak("you system is restarting")
        elif "lock of" in query:
            pyautogui.hotkey("Fn","Esc")
        elif "increase brightness" in query:
            pyautogui.hotkey("Fn","f12")
        elif "decrease brightness" in query:
            pyautogui.hotkey("Fn","f11")
        elif "screen capture" in query:
            pyautogui.hotkey("windows","alt","PrtSc")   
        elif "you need some rest" in query:
            speak("thankyou for using me sir ")
            speak("please call me wake up next time ")
            speak("it was a great time with you sir")
            break
        elif "download current audio playlist" in query:
            pyautogui.hotkey("Ctrl","l")
            pyautogui.hotkey("Ctrl","c")
            pyautogui.hotkey("ctrl","v")
            data=pyperclip.paste()
            link=data
            yt_playlist=Playlist(link)
            speak("the current video downloading started")
            for video in yt_playlist.videos: 
               video.streams.get_highest_resolution().download("C:\\Users\\yashm\\Desktop\\playlist\\ragni")
            print("video downloaded :",video.title)
            print("\nall videos are downloaded")
            speak("The current playlist is downloaded successsfully")  
        elif "download old playlist" in query:
            pyautogui.hotkey("Ctrl","l")
            pyautogui.hotkey("Ctrl","c")
            pyautogui.hotkey("ctrl","v")
            data=pyperclip.paste()
            link=data
            yt_playlist=Playlist(link)
            speak("the current video downloading started")
            for video in yt_playlist.videos: 
               video.streams.get_highest_resolution().download("C:\\Users\\yashm\\Desktop\\playlist\\old songs")
            print("video downloaded :",video.title)
            print("\nall videos are downloaded")
            speak("the current playlist is downloaded successsfully")
        elif "download audio playlist" in query:
            pyautogui.hotkey("Ctrl","l")
            pyautogui.hotkey("Ctrl","c")
            pyautogui.hotkey("ctrl","v")
            data=pyperclip.paste()
            print("audio songs started downloading")
            speak("audio songs is strated downloading")
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