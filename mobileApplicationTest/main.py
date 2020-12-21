from kivy.app import App
from kivy.uix.button import Button
from HondaHackathon.app.resources.speech_to_text import speech_to_text
from HondaHackathon.app.resources.text_to_speech import text_to_speech
from HondaHackathon.app.resources.track_car import track_car
from HondaHackathon.app.resources.capture_stealer import capture_stealer
from HondaHackathon.app.resources.fetch_nearest_police_station import fetch_nearest_police_station
from HondaHackathon.app.resources.fetch_nearest_toll_location import fetch_nearest_toll_location
from HondaHackathon.app.utils.string_matching import similar_string
import re

SUCCESS_MESSAGES = {
    "INTRO_COMMAND": "Hi! How can I help you?",
    "CAPTURE_STEALER_REPORTED": "Car stealer was successfully reported.",
    "REPORT_INFO":  "Would you like to know the address of nearest police station?",
    "TOLL_INFO":  "Would you like to know the address of nearest toll station?",
    "TOLL_ORIGIN": "Please convey the origin",
    "TOLL_DESTINATION": "Please convey the destination"
}

ERROR_MESSAGES = {
    "COMMAND_NOT_FOUND": "I am not sure I understand.",
    "CAR_NOT_FOUND":  "I am unable to find the location of your car.",
    "CAPTURE_STEALER_FAILED": "I am unable to report the car stealer",
    "POLICE_STATION_NOT_FOUND":  "I am unable to find the nearest location of a police station.",
    "TOLL_STATION_NOT_FOUND": "I am unable to find the nearest location of a toll station.",
}

COMMANDS = {
    "TRACK_CAR":  'track car' or 'find car' or 'locate car' or 'car stolen',
    "CAPTURE_STEALER": 'capture stealer' or 'contact police' or 'contact toll'
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
        elif re.search(COMMANDS["CAPTURE_STEALER"], command):
            similarity = similar_string(a=command, b=COMMANDS["TRACK_CAR"])
            print("similarity:", similarity)

            if similarity is True:
                state = capture_stealer(mobId=self.mobId)
                if state is True:
                    text_to_speech(speech=SUCCESS_MESSAGES["CAPTURE_STEALER_REPORTED"])
                    text_to_speech(speech=SUCCESS_MESSAGES["REPORT_INFO"])
                    command = speech_to_text()
                    if re.search('Yes' or 'Ok', command):
                        police_location = fetch_nearest_police_station()
                        if police_location:
                            text_to_speech(speech=police_location)
                        else:
                            text_to_speech(speech=ERROR_MESSAGES['POLICE_STATION_NOT_FOUND'])
                    else:
                        text_to_speech(speech=ERROR_MESSAGES["COMMAND_NOT_FOUND"])
                    text_to_speech(speech=SUCCESS_MESSAGES["TOLL_INFO"])
                    command = speech_to_text()
                    if re.search('Yes' or 'Ok', command):
                        text_to_speech(speech=SUCCESS_MESSAGES['TOLL_ORIGIN'])
                        origin = speech_to_text()
                        text_to_speech(speech=SUCCESS_MESSAGES['TOLL_DESTINATION'])
                        destination = speech_to_text()
                        toll_location = fetch_nearest_toll_location(origin, destination)
                        if toll_location is not None:
                            text_to_speech(speech=toll_location)
                        else:
                            text_to_speech(speech=ERROR_MESSAGES['TOLL_STATION_NOT_FOUND'])
                    else:
                        text_to_speech(speech=ERROR_MESSAGES["COMMAND_NOT_FOUND"])
                else:
                    text_to_speech(speech=ERROR_MESSAGES["CAPTURE_STEALER_FAILED"])
            else:
                text_to_speech(speech=ERROR_MESSAGES["COMMAND_NOT_FOUND"])
        else:
            pass


if __name__ == '__main__':
    app = ButtonApp()
    app.run()