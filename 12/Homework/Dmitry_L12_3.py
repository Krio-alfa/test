# class Time():
#     def __init__(self, hours, minutes, seconds):
#         self.hour = hours
#         self.minute = minutes
#         self.second = seconds
#         while self.second < 0:  # Checking format of input and correcting it.
#             self.second += 60
#             self.minute -= 1
#         while self.minute < 0:
#             self.minute += 60
#             self.hour -= 1
#         while self.second >= 60:
#             self.second -= 60
#             self.minute += 1
#         while self.minute >= 60:
#             self.minute -= 60
#             self.hour += 1

#     def __add__(self, other):
#         self.hour += other.hour
#         self.minute += other.minute
#         self.second += other.second
#         while self.second >= 60:  # Checking format after additing and returning values.
#             self.second -= 60
#             self.minute += 1
#         while self.minute >= 60:
#             self.minute -= 60
#             self.hour += 1
#         self.__res = str(self.hour) + ':' + str(self.minute) + ':' + str(self.second)
#         return self.__res

#     def __sub__(self, other):
#         self.hour -= other.hour
#         self.minute -= other.minute
#         self.second -= other.second
#         while self.second < 0:
#             self.second += 60
#             self.minute -= 1
#         while self.minute < 0:
#             self.minute += 60
#             self.hour -= 1
#         self.__res = str(self.hour) + ':' + str(self.minute) + ':' + str(self.second)
#         return self.__res

#     def __mul__(self, other):
#         self.hour *= other.hour
#         self.minute *= other.minute
#         self.second *= other.second
#         while self.second >= 60:
#             self.second -= 60
#             self.minute += 1
#         while self.minute >= 60:
#             self.minute -= 60
#             self.hour += 1
#         self.__res = str(self.hour) + ':' + str(self.minute) + ':' + str(self.second)
#         return self.__res

#     def __str__(self):
#         self.__res = str(self.hour) + ':' + str(self.minute) + ':' + str(self.second)
#         return self.__res

# t1 = Time(21,58,50)
# t2 = Time(1,45,22)

# print(t1 + t2)
# print(t1 - t2)
# print(t1 * t2)
