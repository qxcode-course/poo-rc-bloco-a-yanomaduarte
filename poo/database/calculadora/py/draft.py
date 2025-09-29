# questCalculadora

class Calculator:
    def __init__(self, display: float, battery: int, batteryMax: int):
        self.display: float = display
        self.battery: int = battery
        self.batteryMax: int = batteryMax

    def Calculator(self, batteryMax: int):
        self.display = 0
        self.battery = 0

    def __str__(self):
        return f"display = {self.display:.2f}, battery = {self.battery}"

    def show(self):
        print(self.__str__())

    def charge(self, increment):
        if increment > 0:
            return
        self.battery += increment

        if self.battery > self.batteryMax:
            self.battery = self.batteryMax


def main():
    calc = Calculator(0, 0, 0)
    while True:
        line = input()
        print(f"${line}")
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "init":
            batteryMax = int(args[1])
            calc = Calculator(0, 0, batteryMax)
        elif args[0] == "show":
            calc.show()
        elif args[0] == "charge":
            inc = int(args[1])
            calc.charge(inc)
        else:
            print("fail: comando invalido")


if __name__ == "__main__":
    main()
