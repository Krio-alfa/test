# # Homework
# class Timer:
#     def __init__(self, h, m, s):
#         self.__nhours = int(h)  # Определяем вводные значения.
#         self.__nminutes = int(m)
#         self.__nseconds = int(s)
#         self.__hours = self.__nhours  # Создаём переменные для арифметических действий.
#         self.__minutes = self.__nminutes
#         self.__seconds = self.__nseconds

#     def __str__(self):
#         self.strhours = self.__hours  # Для вывода str.
#         if self.__hours == 0:  # Фиксуем правильный формат.
#             self.strhours = '00'
#         self.strminutes = self.__minutes
#         if self.__minutes == 0:
#             self.strminutes = '00'
#         self.strseconds = self.__seconds
#         if self.__seconds == 0:
#             self.strseconds = '00'
#         self.__hours = self.__nhours  # Сбрасываем таймер.
#         self.__minutes = self.__nminutes
#         self.__seconds = self.__nseconds
#         return str(self.strhours) + ':' + str(self.strminutes) + ':' + str(self.strseconds)

#     def next_second(self):
#         self.__seconds += 1
#         if self.__seconds >= 60:  # Проверка на изменения.
#             self.__minutes += 1
#             self.__seconds = 0  # Сбрасываем секунды.
#         if self.__minutes >= 60:
#             self.__hours += 1
#             self.__minutes = 0
#         if self.__hours >= 24:
#             self.__hours = 0
#             self.__minutes = 0
#             self.__seconds = 0
            
#     def prev_second(self):
#         self.__seconds -= 1
#         if self.__seconds < 00:  # Фиксируем формат и применяем изменения.
#             self.__minutes -= 1
#         if self.__minutes < 00:
#             self.__hours -= 1
#         if self.__hours < 00:
#             self.__seconds = 59
#             self.__minutes = 59
#             self.__hours = 23


# timer = Timer(23, 59, 59)
# print(timer)
# timer.next_second()
# print(timer)
# timer.prev_second()
# print(timer)
        