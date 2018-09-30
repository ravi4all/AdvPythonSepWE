class Car():

    # def __init__(self,color, brand, gear, hybrid):
    #     self.color = color
    #     self.brand = brand
    #     self.gear = gear
    #     self.hybrid = hybrid

    def __init__(self):
        self.color = 'Red'
        self.brand = 'BMW'
        self._gear = False
        # self.__hybrid = True

    def showDetails(self,hybrid):
        # print("Color : {}".format(self.color))
        # print("Brand : {}".format(self.brand))
        # print("Gear : {}".format(self.gear))
        print("Hybrid : {}".format(hybrid))

class Car_1(Car):

    def __init__(self, average, speed):
        self.average = average
        self.speed = speed
        # calling parent constructor
        super().__init__()

    # Function Overriding
    def showDetails(self):
        print("Color : {}".format(self.color))
        print("Brand : {}".format(self.brand))
        print("Gear : {}".format(self._gear))

    def newFeatures(self):
        print("-------New Features-------")
        print("Average : {}".format(self.average))
        print("Speed : {}".format(self.speed))

obj= Car_1(15,300)
Car.showDetails(obj,True)
obj.showDetails()
obj.newFeatures()