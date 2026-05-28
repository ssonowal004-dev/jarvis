import requests
import subprocess
import time


OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL_NAME = "phi3"


# =========================
# START OLLAMA
# =========================

def start_ollama():

    try:

        requests.get("http://localhost:11434")

        print("Ollama already running")

    except:

        print("Starting Ollama...")

        subprocess.Popen(
            ["ollama", "serve"],
            shell=True
        )

        time.sleep(5)


# =========================
# ASK AI
# =========================

def ask_ai(prompt):

    try:

        response = requests.post(

            OLLAMA_URL,

            json={

                "model": MODEL_NAME,

                "prompt": prompt,

                "stream": False
            }

        )

        data = response.json()

        return data["response"]


    except Exception as e:

        print("AI Error:", e)

        return (
            "Sorry sir. "
            "There was an issue with my AI brain."
        )