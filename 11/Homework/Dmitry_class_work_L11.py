# for i in range(5):
#     print(i)

# class Fib:
#     def __init__(self,nn):
#         print("__init__")
#         self.__n = nn
#         self.__i = 0
#         self.__p1 = self.__p2 = 1

#     def __iter__(self):
#         print("__iter__")
#         return self

#     def __next__(self):
#         print("__next__")
#         self.__1 += 1
#         if self.__i > self.__n:
#             raise StopIteration
#         if self.__i in [1, 2]:
#             return 1
#         ret = self.__p1 + self.__p2
#         self.__p1, self.__p2, = self.__p2, ret
#         return ret


# for i in Fib(10):
#     print(i)



# class Class:
#     def __init__(self, n):
#         self.__iter = Fib(n)

#     def __iter__(self):
#         print("Class iter")
#         return self.__iter


# obj = Class(8)

# for i in obj:
#     print(i)


# def fun(n):
#     for i in range(n):
#         yield i


# for v in fun(5):
#     print(v)

# def powers_of_2(n):
#     power = 1
#     for i in range(n):
#         yield power
#         power *=2

# t = list(powers_of_2(8))
# print+(t)


# the_list = [1 if x % 2 == 0 else 0 for x in range(10)]

# print(the_list)


# two = lambda: 2
# sqr = lambda x: x*x
# pwr = lambda x, y: x ** y

# for a in range(2, 3):
#     print(sqr(a), end=' ')
#     print(pwr(a, two()))


# list_1 =[x for x in range(5)]
# list_2 = list(map(lambda x: 2**x, list_1))

# for x in map(lambda x: x*x, list_2):
#     print(x, end=' ')  
# print()


# from random import seed, randint

# seed()
# data = [randint(-10,10) for x in range(5)]
# filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

# print(data)
# print(filtered)


# def outer(par):
#     loc = par

#     def inner():
#         return loc
#     return inner


# var = 1
# fun = outer(var)
# print(fun())


# class Vowels:
#     def __init__(self):
#         self.vow = 'aeiouy '

#         self.pos = 0

#     def __iter__(self):
#         if self.pos == len(self.vow):
#             raise StopIteration
#         self.pos += 1
#         return self.vow[self.pos - 1]

# vowels = Vowels()
# for v in vowels:
#     print(v, end = ' ')


# stream = open('C:/file.txt', mode='r', encoding= None)
# stream.close()

# streaming = open('tzop.txt', 'rt', encoding='utf-8')

# print(streaming.read())
# streaming.close()



# from os import strerror

# srcname = input('Enter the source file name: ')
# try:
#     scr = open(srcname, 'rb')
# except IOError as e:
#     print('Cannot open the source file: ', strerror(e.errno))
#     exit(e.errno)

# dstname = input('Enter the destination file name: ', strerror(e.errno))
# try:
#     dst = open(dstname, 'wb')
# except IOError as e:
#     print('Cannot create the destination file: ', strerror(e.errno))
#     scr.close()
#     exit(e.errno)

# buffer= bytearray(65536)
# total = 0
# try:
#     readin = scr.readinto(buffer)
#     while readin > 0:
#         written = dst.write(buffer[:readin])
#         total += written
#         readin = scr.readinto(buffer)
# except IOError as e:
#     print('Cannot create the destination file', strerror(e.errno))
#     exit(e.errno)

# print(total, 'byte(s) succesfully written')
# scr.close()
# dst.close()
