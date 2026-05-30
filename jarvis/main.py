from voice.whisper_listen import listen
from voice.speak import speak

from brain.ai import (
    ask_ai,
    start_ollama
)

import sys

from router.intent import detect_intent

from router.dispatcher import handle_intent


def is_stop(text):
    stop_words = ["stop", "exit", "quit", "shutdown", "shut down",
                  "bye", "goodbye", "turn off"]
    return any(word in text for word in stop_words)


print("JARVIS INITIALIZING...")


# START AI BRAIN

start_ollama()


speak(
    "Welcome back sir. "
    "Jarvis is online and fully optimized and operational."
)


while True:

    command = listen()

    if not command:

        continue

    command = command.lower().strip()

    print(f"You: {command}")


    # CHECK IF SHUTDOWN COMMAND

    if is_stop(command):

        speak("Goodbye sir. Shutting down.")

        print("JARVIS OFFLINE")

        sys.exit()


    # SIMPLE WAKE RESPONSE

    if command == "jarvis":

        speak(
            "Yes sir. "
            "What should I do next?"
        )

        continue


    # DETECT USER INTENT

    intent = detect_intent(command)

    print(f"Intent: {intent}")


    # HANDLE COMMAND

    response = handle_intent(
        intent,
        command
    )

    print(f"Jarvis: {response}")


    # SPEAK RESPONSE

    speak(response)