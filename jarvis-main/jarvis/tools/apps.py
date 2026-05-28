import os


def open_app(command):

    command = command.lower()


    apps = {

        "notepad": "notepad.exe",

        "calculator": "calc.exe",

        "calc": "calc.exe",

        "chrome": "start chrome",

        "google chrome": "start chrome",

        "youtube": "start https://youtube.com",

        "spotify": "start spotify",

        "paint": "mspaint.exe",

        "cmd": "start cmd",

        "command prompt": "start cmd",

        "vscode": "code",

        "visual studio code": "code"

    }


    for app_name, app_command in apps.items():

        if app_name in command:

            os.system(app_command)

            return f"Opening {app_name}"


    return "Sorry sir, I could not find that application."