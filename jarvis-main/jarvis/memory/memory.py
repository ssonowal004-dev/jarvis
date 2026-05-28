import json


MEMORY_FILE = "memory/memory.json"


def load_memory():

    try:

        with open(MEMORY_FILE, "r") as file:

            return json.load(file)

    except:

        return {}


def save_memory(data):

    with open(MEMORY_FILE, "w") as file:

        json.dump(data, file, indent=4)


def remember(key, value):

    memory = load_memory()

    memory[key] = value

    save_memory(memory)

    return f"I will remember that your {key} is {value}."


def recall(key):

    memory = load_memory()

    return memory.get(
        key,
        f"I don't know your {key} yet."
    )