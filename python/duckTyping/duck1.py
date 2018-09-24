from Wolf import Wolf as w


class Duck:
    def __init__(self, wolf):
        self.speak("Quack! I am born")
        self.wolf = wolf

    def speak(self, message):
        print(self.name + ": " + message)

    def eat(self):
        self.speak(self.wolf.innerVoice("I am eating"))


if __name__ == "__main__":
    d = ducjk
