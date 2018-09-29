Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = "hello"
>>> type(a)
<class 'str'>
>>> isinstance(str, a)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    isinstance(str, a)
TypeError: isinstance() arg 2 must be a type or tuple of types
>>> isinstance(a,str)
True
>>> class Car():
	color = 'red'
	gear = True
	speed = 400
	brand = 'Bmw'

	
>>> Car()
<__main__.Car object at 0x0000023468F7AB70>
>>> car_1 = Car()
>>> car_1
<__main__.Car object at 0x0000023468F7A978>
>>> car_1.speed = 300
>>> car_1.gear = False
>>> car_2 = Car()
>>> car_2.brand
'Bmw'
>>> car_2.speed
400
>>> car_1.average = 20
>>> Car.hybrid = True
>>> car_1.__dict__
{'speed': 300, 'gear': False, 'average': 20}
>>> isinstance(car_1, Car)
True
>>> 
