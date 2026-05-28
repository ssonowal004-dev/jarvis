def detect_intent(command):

    command = command.lower()


    # MEMORY SAVE
    if "remember" in command:

        return "remember"


    # MEMORY RECALL
    elif (
        "what is my" in command
        or "who am i" in command
    ):

        return "recall"


    # OPEN APPS
    elif (
        "open" in command
        or "launch" in command
        or "start" in command
    ):

        return "open_app"


    # YOUTUBE
    elif (
        "play" in command
        or "song" in command
        or "music" in command
        or "youtube" in command
    ):

        return "youtube"


    return "ai_chat"