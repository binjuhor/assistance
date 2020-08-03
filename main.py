import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_brain = ""
robot_ear = speech_recognition.Recognizer()


def assistance_mouth(speak):
    print("Assistance: " + speak)
    robot_mouth = pyttsx3.init()
    robot_mouth.setProperty('rate', 130)
    voices = robot_mouth.getProperty('voices')
    for voice in voices:
        if voice.languages[0] == u'en_US':
            robot_mouth.setProperty('voice', voice.id)
            break
    robot_mouth.say(speak)
    robot_mouth.runAndWait()


while True:
    # Listening
    with speech_recognition.Microphone() as mic:
        print("Assistance: I'm listening")
        audio = robot_ear.listen(mic)
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""

    # @todo: improve by library to make assistance smarter
    print("Assistance: ...")
    if you == "":
        robot_brain = "I can't hear you"
    elif "hello" in you:
        robot_brain = "Hello boss"
    elif "today" in you:
        today = date.today()
        robot_brain = "Today's date " + today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = "Time " + now.strftime("%H hours %M minutes %S Second")
    elif "bye" in you:
        robot_brain = "Good bye Boss"
        assistance_mouth(robot_brain)
        break
    else:
        robot_brain = "I'm fine thank you!"

    assistance_mouth(robot_brain)
