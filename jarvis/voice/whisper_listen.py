import whisper
import speech_recognition as sr


model = whisper.load_model("base")


recognizer = sr.Recognizer()


import re

# FIXED: correct common mishearings after transcription using word boundaries
def fix_text(text):

    fixes = {
        r"\bopen note\b": "open notepad",
        r"\bopen notes\b": "open notepad",
        r"\bopen noted\b": "open notepad",
        r"\bopen noting\b": "open notepad",
        r"\bopen not\b": "open notepad",
        r"\bnote\b": "notepad",
        r"\bclose note\b": "close notepad",
        r"\bclose notes\b": "close notepad",
        r"\bopen calculated\b": "open calculator",
        r"\bopen calculate\b": "open calculator",
        r"\bopen calculating\b": "open calculator",
        r"\bopen cmd\b": "open command prompt",
        r"\bopen command\b(?! prompt)": "open command prompt",
        r"\bopen vs\b": "open vs code",
        r"\bopen visual\b": "open vs code",
    }

    for pattern, correct in fixes.items():
        text = re.sub(pattern, correct, text)

    return text


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

            text = text.lower()
            text = fix_text(text)

            print("You said:", text)

            return text

    except Exception as e:

        print("Listening Error:", e)

        return ""