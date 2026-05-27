def detect_intent(command):

    command = command.lower().strip()


    # CLOSE APPS FIRST
    # IMPORTANT

    if command.startswith("close"):

        return "close_app"


    # OPEN APPS

    elif command.startswith("open"):

        return "open_app"


    # GOOGLE SEARCH

    elif "search google for" in command:

        return "google_search"


    # YOUTUBE SEARCH

    elif "search youtube for" in command:

        return "youtube_search"


    # PLAY MUSIC / VIDEO

    elif command.startswith("play"):

        return "play_youtube"


    # AI CHAT

    else:

        return "ai_chat"