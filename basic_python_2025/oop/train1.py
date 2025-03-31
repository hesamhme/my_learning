class Animal():
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
    
    def make_sound(self):
        print(self.sound)

    def zoo_name(self, zoo_name):
        print(f"{self.zoo_name} is in the zoo")

    def info(self):
        return f"{self.name} is a {self.species} and is {self.age} years old and says {self.sound}"
    
    def __str__(self):
        return f"{self.name} is a {self.species} and is {self.age} years old and says {self.sound}"
        

class Bird(Animal):
    def __init__(self, name, species, age, sound, wingspan):
        super().__init__(name, species, age, sound)
        self.wingspan = wingspan

    def make_sound(self):
        print(f"{self.sound} and flaps wings")

lion = Animal("Simba", "Lion", 5, "Roar")
print(lion.name, lion.species, lion.age, lion.sound)
