import pywhatkit


def play_youtube(command):

    try:

        command = command.lower()


        remove_words = [
            "play",
            "youtube",
            "song",
            "music",
            "video"
        ]


        song = command


        for word in remove_words:

            song = song.replace(word, "")


        song = song.strip()


        if song == "":

            return "Please tell me what you want to play sir."


        pywhatkit.playonyt(song)

        return f"Playing {song} on YouTube"


    except Exception as e:

        print("YouTube Error:", e)

        return "Sorry sir, I could not play the video."