import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
#import googletrans as translator

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#translater = translator()
#out=translater.translate("आप कैसे हैं", dest="en")
#print(out)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return(command)

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Cuurrent time is ' + time)

    elif 'search' in command:
        person = command.replace('search', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'cook' in command:
        talk("No i dont cook, i just swiggy")

    elif 'joke' in command:
        talk(pyjokes.get_joke())
    
    else:
        talk('Please say it again')

#while True:    (run in loop)

run_alexa()