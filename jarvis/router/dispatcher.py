from tools.apps import (
    open_application,
    close_application,
    search_google,
    search_youtube,
    play_youtube
)

from brain.ai import ask_ai

from memory.memory import remember, recall


def handle_intent(intent, command):

    # REMEMBER
    if intent == "remember":

        command = command.lower()

        command = command.replace("remember", "").replace("that", "").replace("my", "").strip()

        if " is " in command:

            key, value = command.split(" is ", 1)

            return remember(
                key.strip(),
                value.strip()
            )

        return "Please tell me what to remember."


    # RECALL
    elif intent == "recall":

        command = command.lower()

        key = command.replace(
            "what is my",
            ""
        ).replace("who am i", "name").replace("that", "").replace("my", "").strip()

        return recall(key)


    # OPEN APP

    elif intent == "open_app":

        return open_application(command)


    # CLOSE APP

    elif intent == "close_app":

        return close_application(command)


    # GOOGLE SEARCH

    elif intent == "google_search":

        return search_google(command)


    # YOUTUBE SEARCH

    elif intent == "youtube_search":

        return search_youtube(command)


    # PLAY YOUTUBE

    elif intent == "play_youtube":

        return play_youtube(command)


    # AI CHAT

    elif intent == "ai_chat":

        return ask_ai(command)


    return "I don't understand the command."