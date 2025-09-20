class Animal:
    def __init__(self, species: str, age: int, sound: str):
        self.species: str = species
        self.sound: str = sound
        self.age: int

    def Animal(self, species: str, sound: str):
        self.species = species
        self.sound = sound

    def makeSound(self) -> str:
        if(self.age == 0):
            return "---"

        if(self.age == 4):
            return "RIP"

        return self.sound
    def ageBy(self, age: int) -> None:
        if(self.age + age >= 4):
            self.age = 4
            print(f"warning: {self.species} morreu")
