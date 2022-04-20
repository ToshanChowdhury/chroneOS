import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import platform

ask_name = open("data/name.txt")
ask_nm = ask_name.read()

age = open("data/age.txt")
ag = age.read()

engine_var = pyttsx3.init()
listener_var = sr.Recognizer()
voices_var = engine_var.getProperty("voices")
engine_var.setProperty("voice", voices_var[1].id)
os_platform = platform.system()
os_release = platform.release()
os_version = platform.version()

def talk(text):
    engine_var.say(text)
    engine_var.runAndWait()

def take_command():
    try:
        with sr.Microphone() as SOURCE:
            print("Listenting...")
            voice_var = listener_var.listen(SOURCE)
            command_var = listener_var.recognize_google(voice_var)
            command_var = command_var.upper()
            print(command_var)
    except:
        pass
    return command_var

def run_speakassist():
    command_var = take_command()
    print(command_var)
    if "PLAY" in command_var:
        song_var = command_var.replace("PLAY", "")
        talk("playing" + " " + song_var)
        pywhatkit.playonyt(song_var)
    elif "TIME" in command_var:
        time_var = datetime.datetime.now().strftime("%I:%M %p")
        talk("The current time is: " + time_var)
        print(time_var)
    elif "DATE" in command_var:
        date_var = datetime.datetime.now().strftime("%d/%m%y")
        talk("The current date is: " + date_var)
        print("The current date is: " + date_var) 
    elif "WHO IS" in command_var:
        person_var = command_var.replace("WHO IS", "")
        info_var = wikipedia.summary(person_var, 1)
        talk(info_var)
        print(info_var)
    elif "JOKE" in command_var:
        joke = talk(pyjokes.get_joke())
        print(joke)
    elif "ARE YOU SINGLE" in command_var:
        talk("I am in relationship with" + " " + os_platform + " " + os_release + " " + os_version)
        print("I am in relationship with" + " " + os_platform + " " + os_release + " " + os_version)
    elif "AM I" in command_var:
        talk("Your Name is: " + " " + ask_nm)
        print("Your Name is: " + " " + ask_nm)
    elif "AGE" in command_var:
        talk("Your Age is:" + " " + ag)
        print("Your Age is: " + " " + ag)
    elif "WHO ARE YOU" in command_var:
        talk("I am SpeakAssist.")
        print("I am SpeakAssist.")
    elif "HOW ARE YOU" in command_var:
        talk("I am fine, thank you.")
        print("I am fine, thank you.")
    else:
        talk("I don't have the command in my command list!!")

while True:
    run_speakassist()