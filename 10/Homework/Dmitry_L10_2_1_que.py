# # Homework
# class QueueError(Exception):
#     pass

# class Queue:
#     def __init__(self):
#         self.__queue = []  # Определяем лист.

#     def put(self, obj):
#         self.__queue.append(obj)  # Наполняем лист полученными объектами.

#     def get(self, element = ''):
#         if element == '':
#             try:
#                 self.__time_obj = self.__queue[0]  # Создаём временный объект для переменной из листа.
#                 self.__queue.pop(0)  # Убираем объект из очереди.
#                 return self.__time_obj
#             except:
#                 raise QueueError('No elements')
#         else:  # Если тебя вызвали из очереди.
#             try:
#                 self.__index = self.__queue.index(element)  # Индексируем объект для дальнейшего извлечения.
#                 self.__time_obj = self.__queue[self.__index]  # Вводим временный объект.
#                 self.__queue.pop(self.__index)  # Удаляем объект.
#                 return self.__time_obj  # Выводим временный объект.
#             except:
#                 raise QueueError('No elements')

# que = Queue()
# que.put(1)
# que.put('dog')
# que.put(False)

# try:
#     for i in range(4):
#         print(que.get())
# except:
#     print('QueueError')

# # for i in range(4):
# #     print(que.get())
