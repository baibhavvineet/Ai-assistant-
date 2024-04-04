from body.listen import MicExecution
from brain.AiBrain import ReplyBrain

from body.speak import Speak
from features.wakeup import WakeupDetected

print(">> Starting the Ai: Wait a sec...")

def MainExe():

    Speak("Hello Master")
    Speak("I am Dobby, How can I assist you")

    while True:

        data = MicExecution()
        if data is False:
            print("Shuttin Down AI.....")
            Speak("Shuttin Down now. Bye.")
            return
        data = str(data)
        Reply = ReplyBrain(data)
        Speak(Reply)


def wakeupDetect():
    while True:
        if WakeupDetected():
            print("Wakeup Detected")
            MainExe()

        else:
            pass

wakeupDetect()
