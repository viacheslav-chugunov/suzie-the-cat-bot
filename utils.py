import random


def get_suzie_photo():
    result = random.randrange(1, 63)
    return open(f"assets/cat/{result}.jpg", "rb")


def interact_with_suzie(action: str):
    result = random.randrange(0, 100)
    if action == "Pet":
        if result < 33:
            return "Suzie says \"Murr\" and begins to flip from side to side. 😽"
        elif result < 66:
            return "Suzie slowly lies on her belly and closes her eyes. 😸"
        else:
            return "Suzie quickly gets up and runs away. 🐈‍⬛"
    elif action == "Feed":
        if result < 33:
            return "Suzie looks at the food but doesn't eat, she doesn't seem to be hungry. 🐈‍⬛"
        if result < 66:
            return "Suzie goes to eat. After eating, she licks herself, lies on her side and falls asleep. 😸"
        else:
            return "Suzie quickly seizes everything from the bowl and asks for more. 😼"
    elif action == "Play":
        if result < 33:
            return "Suzie starts running around the apartment. You try to catch up with her, but she hides under the " \
                   "bed. 😺"
        if result < 66:
            return "Suzie hides behind boxes and starts wagging her tail. 😸"
        else:
            return "Suzie doesn't react to you. 🐈‍⬛"
    else:
        return "Suzie did not hear your and she continues to see into the void yet... 🐱"
