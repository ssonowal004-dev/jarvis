from tools.apps import (
    open_application,
    close_application,
    search_google,
    search_youtube,
    play_youtube
)

from brain.ai import ask_ai


def handle_intent(intent, command):

    # OPEN APP

    if intent == "open_app":

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