import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()
robot_brain = ""
while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic)

    print("Robot:...")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("you:" + you)

    if you == "":
        robot_brain = "I can't hear you, try again"
    elif "hello" in you:
        robot_brain = "Hello Loc"
    elif "today" in you:
        robot_brain = date.today().strftime("%B %d, %Y")
    elif "time" in you:
        robot_brain = datetime().now().strftime("%H hours %M minutes %S seconds")
    elif "bye" in you:
        robot_brain = "Bye Loc"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "I'm fine thanks"

    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()