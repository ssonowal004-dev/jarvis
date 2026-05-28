import pyttsx3


def speak(text):

    try:

        engine = pyttsx3.init()

        engine.setProperty("rate", 170)

        voices = engine.getProperty("voices")

        engine.setProperty("voice", voices[0].id)

        print("Jarvis:", text)

        engine.say(text)

        engine.runAndWait()

        engine.stop()

    except Exception as e:

        print("Voice Error:", e)


def stop_speaking():

    pass