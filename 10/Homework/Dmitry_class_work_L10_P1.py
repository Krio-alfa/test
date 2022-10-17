# class Classy:
#     def method(self, par):
#         print("method: " + par)

# obj = Classy()
# obj.method(1)
# obj.method(2)
# obj.method(3)


# class variable:
#     varia = 2
#     var = 0
#     def other(self):
#         print("other")
    
#     def num(self):
#         print(self.varia, self.var)


# obj = variable()
# obj.var = 3
# obj.other()
# obj.num()


# class C:
#     def __init__(self, value):
#         self.var = value


# obg_l = C()

# print(obg_l.var)


# class B:
#     def visible(self):
#         print('visible')
    
#     def __hidden(self):
#         print('hidden')

# obj_s = B()
# obj_s.visible()

# try:
#     obj_s.__hidden()
# except:
#     print('failed')

# obj_s._B__hidden()

# print(obj_s.__dict__)

# print(B.__dict__)


# class Sample:
#     def __init__(self):
#         self.name = Sample.__name__

#     def myself(self):
#         print('My name is' + self.name + ' living in a ' + Sample.__module__)

# obj_k = Sample()
# obj_k.myself()


# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy

#     def __str__(self):
#         return self.name + 'in' + self.galaxy


# sun = Star('Sun', 'Milky Way')
# print(sun)
