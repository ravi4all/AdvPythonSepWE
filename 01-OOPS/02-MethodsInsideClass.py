class Car():
    # Data Members
    color = 'red'
    brand = 'BMW'
    gear = True
    speed = 300

    def showDetails(self):
        print("Car Details :")
        print("Speed : {}, Gear : {}, Color : {}".format(self.speed, self.gear, self.color))

car_1 = Car()
car_1.speed = 400
car_1.gear = False
car_1.showDetails()