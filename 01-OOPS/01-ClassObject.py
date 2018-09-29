class Car():
    """This is class car"""
    # Data Members
    color = 'red'
    brand = 'BMW'
    gear = True
    speed = 300

car_1 = Car()
print("Car Details :")
print("Speed : {}, Gear : {}, Color : {}".format(car_1.speed, car_1.gear, car_1.color))
car_1.speed = 400
car_1.gear = False
# Directory
# print(car_1.__dir__())
# Print the name of class
# print(car_1.__class__)
# Print the variables
# print(car_1.__dict__)
# Document String
print(car_1.__doc__)