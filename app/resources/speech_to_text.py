import speech_recognition as sr

ERROR_MESSAGES = {
    "TEXT_NOT_FOUND": "I am not sure I understand.",
    "S2T_NOT_WORKING":  "There seems to be a technical issue. Can you please repeat?"
}


def speech_to_text():
    """
    Take speech as input
    :return: recognized text
    """
    try:
        r = sr.Recognizer()
        print("Speech recognizer activated:::::::::::::")

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            text = r.listen(source, timeout=10)

            try:
                recognized_text = r.recognize_google(text)
                print(recognized_text)
                if not recognized_text or recognized_text is "" or None:
                    recognized_text = ERROR_MESSAGES["TEXT_NOT_FOUND"]
            except sr.UnknownValueError as u:
                print(u)
                recognized_text = ERROR_MESSAGES["TEXT_NOT_FOUND"]
            except sr.RequestError as e:
                print(e)
                recognized_text = ERROR_MESSAGES["TEXT_NOT_FOUND"]
    except Exception as e:
        print(e)
        recognized_text = ERROR_MESSAGES["S2T_NOT_WORKING"]
    return recognized_text


if __name__ == '__main__':
    speech_to_text()
