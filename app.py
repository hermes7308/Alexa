import pywhatkit

from alexa import Alexa


def play_youtube(command):
    song = command.replace('play', '')
    Alexa.talk('playing ' + song)
    pywhatkit.playonyt(song)


command_map = {
    "play": play_youtube
}

if __name__ == "__main__":
    arun = Alexa(command_map)
    arun.run()
