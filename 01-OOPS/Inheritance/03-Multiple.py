class Car():

    def __init__(self,color, brand, gear):
        self.color = color
        self.brand = brand
        self.gear = gear

    def showDetails(self):
        print("Color : {}".format(self.color))
        print("Brand : {}".format(self.brand))
        print("Gear : {}".format(self.gear))

class Car_1():

    def __init__(self, average, speed, hybrid):
        self.average = average
        self.speed = speed
        self.hybrid = hybrid

    def newFeatures(self):
        print("-------New Features-------")
        print("Average : {}".format(self.average))
        print("Speed : {}".format(self.speed))

    def showDetails(self,hybrid):
        print("Hybrid : {}".format(self.hybrid))

# Multiple
class Car_11(Car,Car_1):

    def __init__(self,average, speed, hybrid, color, brand, gear):
        self.average = average
        self.speed = speed

        super().__init__(color, brand, gear)
        Car_1.__init__(self,average,speed, hybrid)

    def updatedFeatures(self):
        print("-----Updated Features-----")
        print("Updated Average : {}".format(self.average))
        print("Updated Speed : {}".format(self.speed))

obj = Car_11(15,300,True,'Red','BMW',False)
obj.showDetails()
obj.newFeatures()
obj.updatedFeatures()