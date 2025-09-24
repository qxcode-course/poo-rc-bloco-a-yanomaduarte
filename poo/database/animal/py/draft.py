class Animal:
    def __init__(self, species: str, sound: str):
        self.species: str = species
        self.sound: str = sound
        self.age: int = 0

    def Animal(self, species: str, sound: str):
        self.species = species
        self.sound = sound

    def ageBy(self, increment: int) -> None:
        if self.age >= 4:
            print(f"warning: {self.species} morreu")
            return

        self.age += increment
        if self.age >= 4:
            self.age = 4
            print(f"warning: {self.species} morreu")

    def makeSound(self) -> str:
        if self.age == 0:
            return "---"
        elif self.age == 4:
            return "RIP"
        else:
            return self.makeSound()

    def __str__(self) -> str:
        return f"{self.species}:{self.age}:{self.sound}"


def main() -> None:
    animal = Animal("", "")
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
            species: str = args[1]
            sound: str = args[2]
            animal = Animal(species, sound)
        elif args[0] == "fazer":
            print(animal.makeSound())
        elif args[0] == "grow":
            age: int = int(args[1])
            animal.ageBy(age)
        elif args[0] == "show":
            print(animal)
        else:
            print("fail: comando não encontrado")


if __name__ == "__main__":
    main()
