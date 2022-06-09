import traceback

import pyttsx3
import speech_recognition as sr

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
DETECT_NAME = "alexa"

class Alexa:
    def __init__(self, command_map):
        self.command_map = command_map

    @staticmethod
    def talk(text):
        engine.say(text)
        engine.runAndWait()

    @staticmethod
    def take_command():
        try:
            with sr.Microphone() as source:
                print('listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if DETECT_NAME in command.lower():
                    command = command.replace(DETECT_NAME, '')
                    print(command)
                    return command
        except Exception:
            pass

        return None

    def run(self):
        while True:
            command = self.take_command()
            if command is None:
                continue

            is_executed = False
            for command_name in self.command_map.keys():
                if command_name in command:
                    job = self.command_map[command_name]
                    job(command)
                    is_executed = True
                    break

            if is_executed is False:
                self.talk("Please say the command again.")
