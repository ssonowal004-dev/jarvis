import speech_recognition as sr


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

    with sr.Microphone() as source:

        print("Listening...")


        # IMPROVE NOISE HANDLING

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )


        # BETTER THRESHOLDS

        recognizer.pause_threshold = 1.2

        recognizer.energy_threshold = 300


        try:

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=8
            )

            print("Recognizing...")


            command = recognizer.recognize_google(
                audio
            )

            command = command.lower()
            command = fix_text(command)

            print(f"You said: {command}")

            return command


        except sr.WaitTimeoutError:

            return ""


        except sr.UnknownValueError:

            print("Could not understand audio")

            return ""


        except sr.RequestError:

            print("Internet issue")

            return ""


        except Exception as e:

            print(e)

            return ""