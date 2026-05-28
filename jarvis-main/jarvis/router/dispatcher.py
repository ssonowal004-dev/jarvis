from tools.apps import open_app

from tools.youtube import play_youtube

from memory.memory import remember, recall


def dispatch(intent, command):

    try:

        # REMEMBER
        if intent == "remember":

            command = command.lower()

            command = command.replace("remember", "").strip()

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
            ).strip()

            return recall(key)


        # OPEN APP
        elif intent == "open_app":

            return open_app(command)


        # YOUTUBE
        elif intent == "youtube":

            return play_youtube(command)


        else:

            return "Sorry sir, I don't know how to do that yet."

    except Exception as e:

        print("Dispatcher Error:", e)

        return "Sorry sir, something went wrong."