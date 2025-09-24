class Animal:
    def __init__(self, species: str, age: int, sound: str):
        self.species: str = species
        self.sound: str = sound
        self.age: int = age

    def Animal(self, species: str, sound: str):
        self.species = species
        self.sound = sound

    def makeSound(self) -> str:
        if (self.age == 0):
            return "---"

        if (self.age >= 4):
            return "RIP"

        return self.makeSound()

    def ageBy(self, age: int) -> None:
        if (self.age + age >= 4):
            self.age = 4
            print(f"warning: {self.species} morreu")

    def show(self) -> None:
        print(self)

    def __str__(self) -> str:
        return f"{self.species}:{self.age}:{self.sound}"

def main() -> None:
    animal = Animal("", 0, "")
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "criar":
            species: str = args[1]
            age: int = int(args[2])
            sound: str = args[3]
            animal = Animal(species, age, sound)
        elif args[0] == "fazer":
            print(animal.makeSound())
        elif args[0] == "envelhecer":
            age: int = int(args[1])
            animal.ageBy(age)
        elif args[0] == "mostrar":
            print("$" + str(animal))
        else:
            print("fail: comando não encontrado")

main()