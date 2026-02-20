import speech_recognition as sr 
import webbrowser
import pyttsx3
import pyaudio
import musiclibrary
from openai import OpenAI
recognizer=sr.Recognizer()
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def aiprocess(c):
    client = OpenAI(api_key="YOUR_REAL_API_KEY")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Friday."},
            {"role": "user", "content": "What is programming?"}
        ]
    )

    return(response.choices[0].message.content)
def processcommand(c):
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c:
        webbrowser.open("https://instagram.com")
    elif c.startswith("play"):
        song=c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        webbrowser.open("https://edition.cnn.com/")
    else:
        #lets open ai handle after this
        output=aiprocess(command)
        speak(output)
        print(output)
if __name__=="__main__":
    speak("running friday.....")
    while True:
        print("recognizing.....")
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio = recognizer.listen(source, timeout=4, phrase_time_limit=3)
            text = recognizer.recognize_google(audio).lower()
            print("you: ",text)
            if "friday" in text:
                speak("ya")
                #now after waking it up it will listen our our command 
                with sr.Microphone() as source:
                    print("Friday is active")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio).lower()
                    processcommand(command)

        except Exception as e:
            print("Could not request results; {0}".format(e))




