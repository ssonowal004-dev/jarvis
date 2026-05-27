import speech_recognition as sr


recognizer = sr.Recognizer()


def listen():

    with sr.Microphone() as source:

        print("Listening...")


        # IMPROVE NOISE HANDLING

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )


        # BETTER THRESHOLDS

        recognizer.pause_threshold = 1.2

        recognizer.energy_threshold = 300


        try:

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=8
            )

            print("Recognizing...")


            command = recognizer.recognize_google(
                audio
            )

            command = command.lower()

            print(f"You said: {command}")

            return command


        except sr.WaitTimeoutError:

            return ""


        except sr.UnknownValueError:

            print("Could not understand audio")

            return ""


        except sr.RequestError:

            print("Internet issue")

            return ""


        except Exception as e:

            print(e)

            return ""