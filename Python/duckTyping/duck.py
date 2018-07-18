from wolf import Wolf


class Duck:
    def __init__(self, name, wolf):
        self.name = name
        self.speak("Quack! I am born")
        self.wolf = wolf

    def speak(self, message):
        print(self.name + ": " + message)


    def eat(self):
        self.speak(self.wolf.innerVoice("I am eating"))


if __name__ == "__main__":
    w = Wolf("Willy")
    d = Duck("Donaldo", w)
    d.eat()
