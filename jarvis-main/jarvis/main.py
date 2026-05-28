import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from router.intent import detect_intent
from router.dispatcher import dispatch
from voice.whisper_listen import listen
from voice.speak import speak


def is_stop(text):
    stop_words = ["stop", "exit", "quit", "shutdown", "shut down",
                  "bye", "goodbye", "turn off"]
    return any(word in text for word in stop_words)


def run_command(user_input):

    user_input = user_input.strip()

    if not user_input:
        return

    print("You:", user_input)

    intent = detect_intent(user_input)
    print("Intent:", intent)

    try:
        response = dispatch(intent, user_input)
    except Exception as e:
        print("Dispatch error:", e)
        response = "Sorry, something went wrong."

    if not response:
        response = "Done."

    print("Jarvis:", response)
    speak(response)


print("JARVIS ONLINE")
speak("Jarvis online. Ready for your command.")

while True:

    print("\n>>> Listening...")
    user_input = listen()

    if not user_input or user_input.strip() == "":
        continue

    if is_stop(user_input):
        speak("Goodbye sir. Shutting down.")
        print("JARVIS OFFLINE")
        sys.exit()

    run_command(user_input)