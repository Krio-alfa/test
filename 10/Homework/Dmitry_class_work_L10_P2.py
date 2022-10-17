# from ossaudiodev import control_labels
# from statistics import variance
# from tkinter import Variable


# class Venicle:
#     pass

# class LandVehicle(Venicle):
#     pass

# class TrackedVehicle(LandVehicle):
#     pass

# for cls1 in [Venicle, LandVehicle, TrackedVehicle]:
#     for cls2 in [Venicle, LandVehicle, TrackedVehicle]:
#         print(issubclass(cls1, cls2), end="\t")
#     print()



# class Level1:
#     variable_l = 100
#     def __init__(self):
#         self.var = 101

#     def fun_1(self):
#         return 102

# class Level2(Level1):
#     variable_2 = 200
#     def __init__(self):
#         super().__init__()
#         self.var_2 = 201

#     def fun_2(self):
#         return 202

# class Level3(Level2):
#     variable_3 = 300
#     def __init__(self):
#         super().__init__()
#         self.var_3 = 301

#     def fun_3(self):
#         return 302

# obj = Level3()

# print(obj.variable_l, obj.var, obj.fun_1())
# print(obj.variable_2, obj.var_2, obj.fun_2())
# print(obj.variable_3, obj.var_3, obj.fun_3())

# import time

# class TVehicle:
#     def control_track(left, stop):
#         pass

#     def turn(left):
#         control_track(left, True)
#         time.sleep(0.25)
#         control_track(left, False)


# class WVehicle:
#     def turn_front_wheels(left, on):
#         pass

#     def turn(left):
#         turn_front_wheels(left, True)


# class A:
#     pass

# class B(A):
#     pass

# class C(A):
#     pass

# class D(B, C):
#     pass

# d = D()



# def reciorical(n):
#     try:
#         n = 1/n
#     except ZeroDivisionError:
#         print('Division failed')
#         return None
#     else:
#         print('Everything went fine')
#         return n
#     finally:
#         print('Final checkout')

# print(reciorical(2))
# print(reciorical(0))
