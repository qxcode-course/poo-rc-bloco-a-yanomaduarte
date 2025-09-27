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


    