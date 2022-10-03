# import keyword

# # input() function
# print('Enter your name:')
# x = input() # Asking some info from user
# print('Hello, '+x)

# # String cannot convert to int (TypeError).
# number = input('Number:')
# output = number ** 2.0 # Str ** 2 - Error.
# print(number, 'to the power of 2 is', output)

# # Different ways to prevent error.
# num_1 = float(input()) # We convert string to float by float() function.
# num_2 = input()
# num_2 = int(num_2) # We rewrite num_2 to float. (We can convert any variable to string. Int - float. Float - int.)
# # Functions to convert variables int(), float(), str().
# Float = int(2.8) # Will be 2
# z = str(3.0) # Some interesting convertasion. Will be '3.0' 

# # Printing functions
# print("Scientia" + "est" + "potentia") # We use + when we need to add something to text.
# print("James" * 3, '2' * 5, 3 * 'an') # This is replication.
# #Interesting example:
# print('+' + 10 * "-" + "+")
# print(('|' + " " * 10 + "|\n") * 5, end='') # Little table)
# print('+' + 10 * "-" + '+')

# #Examples of formating
# a = 100
# print(f'{a = }') # Output: a = 100
# print('{} {} {}'.format(a, a + 5, a + 10)) # Output: 100 105 110
