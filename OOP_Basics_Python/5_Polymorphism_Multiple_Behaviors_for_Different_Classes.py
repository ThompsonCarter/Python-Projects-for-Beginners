class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

animals = [Dog("Rex"), Cat("Whiskers")]

for animal in animals:
    animal.speak()  # Output: Rex barks. Whiskers meows.