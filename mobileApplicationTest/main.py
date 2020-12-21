from kivy.app import App
from kivy.uix.button import Button
from HondaHackathon.app.resources.speech_to_text import speech_to_text
from HondaHackathon.app.resources.text_to_speech import text_to_speech
from HondaHackathon.app.resources.track_car import track_car
from HondaHackathon.app.utils.string_matching import similar_string
import re

SUCCESS_MESSAGES = {
    "INTRO_COMMAND": "Hi! How can I help you?"
}

ERROR_MESSAGES = {
    "COMMAND_NOT_FOUND": "I am not sure I understand.",
    "CAR_NOT_FOUND":  "I am unable to find the location of your car."
}

COMMANDS = {
    "TRACK_CAR":  'track car' or 'find car' or 'locate car' or 'car stolen'
}


class ButtonApp(App):
    def build(self):
        # TODO: assign a MOBID for user
        self.mobId = "MOBL153HHT0015627"
        return Button()

    def on_press_button(self):
        print('You pressed the button!')
        text_to_speech(speech=SUCCESS_MESSAGES["INTRO_COMMAND"])
        command = speech_to_text()

        if re.search(COMMANDS["TRACK_CAR"], command):
            similarity = similar_string(a=command, b=COMMANDS["TRACK_CAR"])
            print("similarity:", similarity)

            if similarity is True:
                car_location = track_car(mobId=self.mobId)
                if car_location:
                    text_to_speech(speech=car_location)
                else:
                    text_to_speech(speech=ERROR_MESSAGES["CAR_NOT_FOUND"])
            else:
                text_to_speech(speech=ERROR_MESSAGES["COMMAND_NOT_FOUND"])
        else:
            pass


if __name__ == '__main__':
    app = ButtonApp()
    app.run()