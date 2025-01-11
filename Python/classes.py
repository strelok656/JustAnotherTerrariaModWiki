# class Human:
#     name = "Человек"
#     age = 13
#     height = 243
#     def do_barrel_roll(self):
#         print(self.name + " сделал бочку!")
# humanOne = Human()
# humanOne.do_barrel_roll()

# class Ball:
#     color = "Бесцветный"
#     size = 10

#     def __init__(self, color1, size1):
#         self.color = color1
#         self.size = size1

#     def what_ball(self):
#         print(self.color + " мячик размера " + str(self.size) + " сделал прыг!")

# ball = Ball("Черный", 15)
# ball.what_ball()

# class Human:
#     name = ""
#     age = 0
#     height = 5
#     def __init__(self, imya, vozrast, rost):
#         self.name = imya
#         self.age = vozrast
#         self.height = rost

#     def do_barrel_roll(self):
#         print(self.name + " сделал бочку! Ему было " + str(self.age) + " лет!")

# humanOne = Human("Петрович", 45, 178)
# humanOne.do_barrel_roll()

class Car:
    name = "car"

    def speed():
        print("Машина разогналась")

    def fuel():
        print("Машина заправилась")

    def dive():
        print("Машина погрузилась")

class LightCar(Car):
    def __init__(self, name1):
        self.name = name1

    def speed(self):
        print(self.name + " разогналась")

    def fuel(self):
        print(self.name + " заправлена")

class Truck(Car):
    def __init__(self, name1):
       self.name = name1

    def fuel(self):
        print(self.name + " заправился")
    
    def dive(self):
        print(self.name + " погрузился")

class BELAZ(Car):
    def __init__(self, name1):
       self.name = name1
    
    def speed(self):
        print(self.name + " разогнался")
    
    def dive(self):
        print(self.name + " погрузился")

lighty = LightCar("Легковушка")
big_car = Truck("Грузовик")
WHITY = BELAZ("БЕЛАЗ")

lighty.speed()
big_car.fuel()
WHITY.dive()