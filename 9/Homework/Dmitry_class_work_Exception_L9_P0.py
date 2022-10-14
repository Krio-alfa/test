# # That code runs always.
# try:
#     print(6 / 0)  # Trying to launch it.
# except:
#     print("Error happend")  # If errors exists.
# # Back to normal code.

# try:
#     y = 1 / 0
# except ZeroDivisionError:  # If error ZeroDivisionError exists.
#     print("Ooopss...")

# try:
#     y = 1 / 0
# except ArithmeticError:  # This error combine others arithmetic errors, this incude zero error.
#     print("Ooopss...")

# def bad_fun(n):
#     try:
#         return n/0
#     except:
#         print("Some error happend.")
#         raise  # Raising error from function

# try:
#     bad_fun(0)
# except ArithmeticError:  # Catching error from function.
#     print("Yes, it is.")

# import math
# x = float(input("Enter a number:"))
# assert x >= 0.0

# try:
#     print(2/0)
# except ArithmeticError:  # We can use more exceptions but need to look at error.
#     print("arith")
# except ZeroDivisionError:   # This wont work..
#     print("zero")
# except:
#     print("some")


