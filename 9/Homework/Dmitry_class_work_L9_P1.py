# from audioop import add
# from inspect import stack


# class Simpliest:  # This is a class.
#     pass


# MyObject = Simpliest()  # This is object crated by class.

# print(type(MyObject))  # Type will be __main__.Simpliest


# class Stacking:
#     def __init__(self):  # Defining the Stack class.
#         print('Hi!')


# # Creating an object.
# stack_obj = Stacking()
# # Prints Hi! in output.


# class test:
#     def __init__(self):  # Going with initialization.
#         self.stack_list = []  # Defining variable.

# obj = test()

# print(len(obj.stack_list))

# class Stack:
#     def __init__(self):
#         self.__stack_list= []  # Defining variable when inizialized
    
#     def push(self, val):  # Requing val as variable for object to be contained.
#         self.__stack_list.append(val)
    
#     def pop (self):
#         val = self.__stack_list[-1]  # Collecting last var.
#         del self.__stack_list[-1]  # Deleting this var from list.
#         return val


# class additing(Stack):  # Additing inherits Stack.
#     sum = 0
#     def __init__(self):
#         Stack.__init__(self)  # Initialization Stack`s init.
        


# stac = additing()

# print(stac.sum)  # Printing sum.
# stac.push(45)
# stac.push(1)
# stac.push("Hello")  # Additing variables to stack.
# print(stac.pop)  # Calling and deleting last variable.
