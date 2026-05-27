import requests
import subprocess
import time


OLLAMA_URL = "http://localhost:11434/api/generate"


# START OLLAMA AUTOMATICALLY

def start_ollama():

    try:

        # CHECK IF OLLAMA IS RUNNING

        requests.get("http://localhost:11434")

        print("Ollama already running")

    except:

        print("Starting Ollama...")

        subprocess.Popen(
            ["ollama", "run", "phi3"],
            shell=True
        )

        # WAIT FOR OLLAMA TO START

        time.sleep(10)

        print("Ollama started")


# ASK AI

def ask_ai(question):

    payload = {

        "model": "phi3",

        "prompt": (
            "You are Jarvis, Tony Stark's AI assistant. "
            "Reply in short, smart and conversational style.\n\n"
            f"User: {question}\nJarvis:"
        ),

        "stream": False
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload
        )

        data = response.json()

        answer = data.get("response")

        if not answer:

            return (
                "Sorry sir, "
                "I could not generate a response."
            )

        return answer.strip()

    except Exception as e:

        print(f"AI Error: {e}")

        return (
            "Sorry sir, "
            "my AI brain is currently offline."
        )