class Car():

    def __init__(self,color, brand, gear, hybrid):
        self.color = color
        self.brand = brand
        self.gear = gear
        self.hybrid = hybrid

    def showDetails(self):
        print("Color : {}".format(self.color))
        print("Brand : {}".format(self.brand))
        print("Gear : {}".format(self.gear))
        print("Hybrid : {}".format(self.hybrid))

class Car_1(Car):

    def __init__(self, average, speed, hybrid, color, brand, gear):
        self.average = average
        self.speed = speed
        # calling parent constructor
        super().__init__(color, brand, gear, hybrid)

    def newFeatures(self):
        print("-------New Features-------")
        print("Average : {}".format(self.average))
        print("Speed : {}".format(self.speed))

# Multilevel
class Car_11(Car_1):

    def __init__(self,average, speed, hybrid, color, brand, gear):
        self.average = average
        self.speed = speed

        super().__init__(color, brand, gear, hybrid)

    def updatedFeatures(self):
        print("Updated Average : {}".format(self.average))
        print("Updated Speed : {}".format(self.speed))

obj = Car_11(15,300,True,'Red','BMW',False)
obj.showDetails()
obj.newFeatures()
obj.updatedFeatures()