# unlimited number of input
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
# print(add(2, 4, 6, 8, 10))
#
# def calculate(n, **kwargs):
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(key, value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)


# calculate(2, add=3, multiply=5)



# class Car:
#
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.color = kw.get("color")
#         self.seat = kw.get("seat")
#
# my_car = Car(make="Nissan", model="GT", color="Black", sealt="gold")
#
# print(my_car.model)
