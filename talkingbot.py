
// create a talking bot

import speech_recognition as sr
import pyttsx3#convert the audio to text
import pywhatkit#bundle of kitt of take the Q from user
import datetime
import wikipedia
import pyjokes#from jiokes (python joke)

listener=sr.Recognizer()#here we are listening
engine=pyttsx3.init()#converting the voice into text
voices=engine.getProperty('voices')#setting the perporty of Alexa(talking bot)
engine.setProperty('voice',voices[1].id)#0 for male and 1 for female voice
#defination for talk of bot
def talk(text):
    engine.say(text)
    engine.runAndWait()


#command taking from user as Voice
def take_command():
    try:
        with sr.Microphone() as source:#listening from the local system
            print('listening.....')
            voice=listener.listen(source)#saving the voice signal in voice variable
            command=listener.recognize_google(voice)#converting sound singnal in text
            command=command.lower()
            if 'bot' in command:#waht yours bot name (ranjit,alexa,disha like this)#checking whether the command in the bot
                command=command.replace('bot','')
                print(command)
    except:
        print(" I am unable to listen..kindly speak again")
    return command

def run_bot():
    wh=['who','why','how','when','where','whome','what']
    whr=['treading','corona']
    mind=['play','fresh']
    command=take_command()
    print(command)
    if mind in command:
        song=command.replace('play','')
        talk('playing '+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().stftime('%I:%M %P')
        talk("current time is "+time)
    elif "who" in command:
        person=command.replace('who','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif "which" in command:
        person=command.replace('which','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    else:
        talk("am  only a talking bot ...am not got")

while True:
    run_bot()
       