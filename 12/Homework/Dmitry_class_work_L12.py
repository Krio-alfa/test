# from email import message


# class Duck():
#     def __init__(self, height, weight, sex);
#         self.height = height
#         self.weight = weight
#         self.sex = sex

#     def walk(self):
#         pass

#     def quack(self):
#         return print('Quack')

# duckling = Duck(10, 3.4, 'male')
# drake = Duck(25, 3.7, 'male')
# hen = Duck(20, 3.4, 'female')

# print(Duck.__class__)
# print(duckling.__class__)
# print(duckling.sex.__class__)
# print(duckling.quack.__class__)


# class Demo:
#     class_var = 'shared variable'

# d1 = Demo()
# d2 = Demo()

# print(d1.class_var)
# print(d2.class_var)
# print('.' * 20)

# d1.class_var = "I'am messing with the class variable"

# print('contents of d2', d2.__dict__)
# print(d1.class_var)
# print('.' * 20)

# print('contents of d2:',  d2.__dict__)
# print('contenrs of class variable accessed via d2', d2.class_var)

# class Phone:
#     counter = 0

#     def __init__(self, number):
#         self.number = number
#         Phone.counter += 1

#     def call(self, number):
#         message = 'Calling {} using own number {}'.format(number,self.number)
#         return message

# class FixedPhone(Phone):
#     last_SN = 0

#     def __init__(self, number):
#         super().__init__(number)
#         FixedPhone.last_SN += 1
#         self.SN = 'FP - {}'.format(FixedPhone.last_SN)

# class MobilePhone(Phone):
#     last_SN = 0

#     def __init__(self, number):
#         super().__init__(number)
#         FixedPhone.last_SN += 1
#         self.SN= 'MP-{}'.format(MobilePhone.last_SN)

# print('Total number of phone devices created:', Phone.counter)
# print('Creating 2 devices')
# fphone = FixedPhone('555-2368')
# mphone = MobilePhone('01632-960004')

# print('Total number of phone devices created:', Phone.counter)
# print('Total of mobile phones created:', MobilePhone.last_SN)

# print(fphone.call('01632-960004'))
# print('Fixed phone recived "{}" serial number'.format(fphone.SN))
# print('Mobile phone received "{}" serial number'.format(mphone.SN))


# number = 10
# print(number + 20)
# print(number.__add__(20))

# class Wax:
#     def melt(self):
#         print('Wax can be used to form a tool')

# class Cheese:
#     def melt(self):
#         print('Cheese can be eaten')

# class Wood:
#     def fire(self):
#         print('A fire has been started!')

# for element in Wax(), Cheese(), Wood():
#     try:
#         element.melt()
#     except AttributeError:
#         print('No melt() function')
