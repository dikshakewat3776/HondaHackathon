import pyttsx3 as p


def text_to_speech(speech):
    """
    Convert text to speech
    :param speech:
    :return: voice based speech
    """
    try:
        engine = p.init("sapi5")
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[1].id)
        engine.say(speech)
        engine.runAndWait()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    text = "MEOW"
    text_to_speech(speech=text)
