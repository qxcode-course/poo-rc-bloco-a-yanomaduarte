class Animal:
    def __init__(self, species: str, age: int, sound: str):
        self.species: str = species
        self.age: int = 0
        self.sound: str = sound
    
    def makeSound(self, ) -> None:
        print(self.sound)

    def ageBy(self) -> int:
        if self.age == 1:
            return 1
        if self.age == 2:
        

    def show(self) -> None:
        print(f"Species: {self.species}, Age: {self.age}, Sound: {self.sound}") 
    
    def __str__(self) -> str:
        return f"{self.species}:{self.age}:{self.sound}." 