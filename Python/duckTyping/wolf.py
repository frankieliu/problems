class Wolf:
    def __init__(self, name):
        self.name = name
        self.speak("Growl!  I am born")

    def speak(self, message):
        print(self.name + ": " + message)

    def innerVoice(self, message):
        return "(" + self.name + ") " + message

    def eat(self):
        self.speak("I am eating")
