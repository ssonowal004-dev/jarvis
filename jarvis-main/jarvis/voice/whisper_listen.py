import whisper
import speech_recognition as sr


model = whisper.load_model("base")


recognizer = sr.Recognizer()


def listen():

    try:

        with sr.Microphone() as source:

            print("Listening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=8
            )

            print("Recognizing...")

            with open("temp.wav", "wb") as f:

                f.write(audio.get_wav_data())

            result = model.transcribe(
                "temp.wav",
                language="en"
            )

            text = result["text"].strip()

            print("You said:", text)

            return text.lower()

    except Exception as e:

        print("Listening Error:", e)

        return ""