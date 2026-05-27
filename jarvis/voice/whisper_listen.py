import speech_recognition as sr

recognizer = sr.Recognizer()
recognizer.pause_threshold = 0.5
recognizer.phrase_threshold = 0.2
recognizer.non_speaking_duration = 0.2
recognizer.dynamic_energy_threshold = True


# FIXED: correct common mishearings after transcription
def fix_text(text):

    fixes = {
        "open note"         : "open notepad",
        "open notes"        : "open notepad",
        "open noted"        : "open notepad",
        "open noting"       : "open notepad",
        "open not"          : "open notepad",
        "note"              : "notepad",       # FIXED: bare "note" → "notepad"
        "close note"        : "close notepad",
        "close notes"       : "close notepad",
        "open calculated"   : "open calculator",
        "open calculate"    : "open calculator",
        "open calculating"  : "open calculator",
        "open cmd"          : "open command prompt",
        "open command"      : "open command prompt",
        "open vs"           : "open vs code",
        "open visual"       : "open vs code",
    }

    for wrong, correct in fixes.items():
        if wrong in text:
            text = text.replace(wrong, correct)

    return text


def listen():

    with sr.Microphone() as source:

        print(">>> Listening for command...")

        recognizer.adjust_for_ambient_noise(source, duration=0.2)

        try:
            audio = recognizer.listen(
                source,
                timeout=6,
                phrase_time_limit=8
            )
        except sr.WaitTimeoutError:
            print("No speech heard.")
            return ""

    try:
        text = recognizer.recognize_google(audio, language="en-IN").lower()
        text = fix_text(text)          # FIXED: apply corrections
        print("You said:", text)
        return text

    except sr.UnknownValueError:
        print("Could not understand.")
        return ""

    except sr.RequestError as e:
        print("Google Speech error:", e)
        return ""