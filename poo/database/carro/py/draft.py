class Car:
    def __init__(self):
        self.pass_ = 0
        self.km = 0
        self.passMax = 2
        self.gas = 0
        self.gasMax = 100

    def __str__(self):
        return f"pass:{self.pass_}, gas:{self.gas}, km:{self.km}"

    def show(self):
        print(self.__str__())

    def enter(self):
        if self.pass_ < self.passMax:
            self.pass_ += 1
        else:
            print("fail: limite de pessoas atingido.")

    def leave(self):
        if self.pass_ > 0:
            self.pass_ -= 1
        else:
            print("fail: não há ninguem no carro.")
