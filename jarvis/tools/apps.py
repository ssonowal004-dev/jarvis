import os
import webbrowser
import urllib.parse
import pywhatkit


# =========================
# APP DATABASE
# =========================

APPS = {

    # NOTEPAD
    "notepad": {
        "open": "start notepad",
        "close": "notepad.exe"
    },

    # CALCULATOR
    "calculator": {
        "open": "start calc",
        "close": "CalculatorApp.exe"
    },

    # PAINT
    "paint": {
        "open": "start mspaint",
        "close": "mspaint.exe"
    },

    # CHROME
    "chrome": {
        "open": "start chrome",
        "close": "chrome.exe"
    },

    # WORD
    "word": {
        "open": "start winword",
        "close": "WINWORD.EXE"
    },

    # EXCEL
    "excel": {
        "open": "start excel",
        "close": "EXCEL.EXE"
    },

    # POWERPOINT
    "powerpoint": {
        "open": "start powerpnt",
        "close": "POWERPNT.EXE"
    },

    # PHOTOS
    "photos": {
        "open": "start ms-photos:",
        "close": "Photos.exe"
    },

    # VS CODE
    "vs code": {
        "open": "start code",
        "close": "Code.exe"
    },

    # CMD
    "cmd": {
        "open": "start cmd",
        "close": "cmd.exe"
    },

    # YOUTUBE
    "youtube": {
        "open": "https://www.youtube.com",
        "close": None
    },

    # GOOGLE
    "google": {
        "open": "https://www.google.com",
        "close": None
    }
}


# =========================
# FIND APP
# =========================

def find_app(command):

    command = command.lower()

    for app in APPS:

        if app in command:

            return app

    return None


# =========================
# OPEN APPLICATION
# =========================

def open_application(command):

    app = find_app(command)

    if app:

        try:

            open_target = APPS[app]["open"]

            # WEBSITE

            if open_target.startswith("http"):

                webbrowser.open(open_target)

            # WINDOWS APP

            else:

                os.system(open_target)

            return f"Opening {app}"

        except Exception as e:

            print(e)

            return f"Failed to open {app}"

    # FALLBACK TO GOOGLE SEARCH

    try:

        query = command.replace("open", "").strip()

        if query != "":

            url = (
                "https://www.google.com/search?q="
                f"{urllib.parse.quote(query)}"
            )

            webbrowser.open(url)

            return (
                f"I could not find the app. "
                f"Searching {query} on Google."
            )

    except:
        pass

    return "Application not found."


# =========================
# CLOSE APPLICATION
# =========================

def close_application(command):

    app = find_app(command)

    if app:

        process = APPS[app]["close"]

        # WEBSITE CANNOT CLOSE

        if process is None:

            return f"I cannot close {app}"

        try:

            os.system(
                f'taskkill /f /im "{process}"'
            )

            return f"Closing {app}"

        except Exception as e:

            print(e)

            return f"Failed to close {app}"

    return "Application not found."


# =========================
# GOOGLE SEARCH
# =========================

def search_google(command):

    query = (
        command.lower()
        .replace("search google for", "")
        .strip()
    )

    if query == "":

        webbrowser.open("https://google.com")

        return "Opening Google"

    url = (
        "https://www.google.com/search?q="
        f"{urllib.parse.quote(query)}"
    )

    webbrowser.open(url)

    return f"Searching Google for {query}"


# =========================
# YOUTUBE SEARCH
# =========================

def search_youtube(command):

    query = (
        command.lower()
        .replace("search youtube for", "")
        .strip()
    )

    if query == "":

        webbrowser.open("https://youtube.com")

        return "Opening YouTube"

    url = (
        "https://www.youtube.com/results?"
        f"search_query={urllib.parse.quote(query)}"
    )

    webbrowser.open(url)

    return f"Searching YouTube for {query}"


# =========================
# PLAY YOUTUBE VIDEO
# =========================

def play_youtube(command):

    query = command.lower().replace("play", "").strip()

    if query == "":

        query = "trending songs"

    pywhatkit.playonyt(query)

    return f"Playing {query} on YouTube"