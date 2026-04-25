# for this project 3.12 is used 
# first create .venv 
# PS E:\Data Analyst\Python\Mega_Project_1> rmdir /s /q .venv
# PS E:\Data Analyst\Python\Mega_Project_1> py -3.12 -m venv .venv
# PS E:\Data Analyst\Python\Mega_Project_1> .venv\Scripts\Activate.ps1
# (.venv) PS E:\Data Analyst\Python\Mega_Project_1> python --version
# Python 3.12.10
# (.venv) PS E:\Data Analyst\Python\Mega_Project_1> python -m pip install --upgrade pip
# (.venv) PS E:\Data Analyst\Python\Mega_Project_1> pip install speechrecognition pyaudio
#PS E:\Data Analyst\Python\Mega_Project_1> pip install setuptools
#PS E:\Data Analyst\Python\Mega_Project_1> pip install pyttsx3      
# PS E:\Data Analyst\Python\Mega_Project_1> pip install pocketSphinx

#pip install setuptools
import speech_recognition as sr  # as -  you can use sr instead of  speech_recognition
import webbrowser    # this is built-in module
# pip install pyttsx3 
import pyttsx3       # this is for enable offline text-to-speech(TTS) capabilities

#pip install pocketSphinx
import musicLibrary
# import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
'''newsapi = ""  # write here your api key'''


def speak(text):
  engine.say(text)
  engine.runAndWait()

def processCommand(c):
  if "open google" in c.lower():
    webbrowser.open("https://google.com")
  elif "open facebook" in c.lower():
    webbrowser.open("https://facebook.com")
  elif "open youtube" in c.lower():
    webbrowser.open("https://youtube.com")
  elif "open linkdin" in c.lower():
    webbrowser.open("https://linkdin.com")
  elif c.lower().startswith("play"):
    song = c.lower().split(" ")[1]
    link = musicLibrary.music[song]
    webbrowser.open(link)

    # #  elif "news" in c.lower():
#     r = requests.get("")  # here copy link
#     if r.status_code == 200:
#       # parse the JSON response
#       data = r.json()

#       #Extra the articales
#       articles = data.get('article',[])

#       # print the headlines
#       for article in articles:
#         speak(article['title'])  #

  else:
    #let OpenAI handle the request
    pass
  



if __name__ == "__main__":
  speak("Initializing jarvis...")
  while True:
    # Listen for the wake word "Jarvis"
    # obtain audio from the microphone
    r = sr.Recognizer()
    
    
    # recognize speech using 
    print("recognizing...")
    try:
      with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source,timeout=2,phrase_time_limit=3)
      word = r.recognize_google(audio)
      if(word.lower() == "jarvis"):
        speak("Ya")
        # Listen for command
        with sr.Microphone() as source:
          print("Jarvis Active...")
          audio = r.listen(source)
          command = r.recognize_google(audio)

          processCommand(command)

    except Exception as e:
      print("Error; {0}".format(e))
  