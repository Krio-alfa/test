# class Stack:
#     def __init__(self):
#         self.__listed = []
    
#     def push(self, val):
#         self.__listed.append(val)

#     def pop(self):
#         val = self.__listed[-1]
#         del self.__listed[-1]
#         return val

# class CountingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__counter_push = 0
#         self.__counter_pop = 0

#     def pop(self):
#         self.__counter_pop += 1
#         Stack.pop(self)
        
    
#     def push(self, val):
#         self.__counter_push += 1
#         Stack.push(self, val)
        

#     def get_count(self):
#         print("Count of pop: "+ str(self.__counter_pop))
#         print("Count of push: "+ str(self.__counter_push))


# stk = CountingStack()


# for i in range(100):
#     stk.push(1)
#     stk.pop()

# stk.get_count()