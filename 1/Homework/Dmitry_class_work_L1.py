# Printing text.
print('Hello world!')
print('Per aspera ad astra')

# Next line.
print('Its a very long text.\nBut you don`t need to read it...')

# Errors with print funtion.
print("\")" # This isn`t right.
print("\\") # This is right.

# Separation.
print("Hello","new","world!")

# Defining "end" and "sep" meaning.
print('Testing','unusual','programs',sep='-') # Sep between columns.
print('Never forget the end',end=')))\n') # Writing at the end of print.

# Data + Variables.
a = 10 # Integer.
b = 0o231 # Octal.
c = 0x123 # Hexadecimal.
d = 8.3 # Floats.
e = 3E8 # Scientific Stuff.
f = "Hi" # String.
g = True # Boolen.
# Variable have to be without spaces, no system names, ALWAYS check register, it is didn`t matter long or short name.
x = "Hello"
x = "John" # We can rewrite variables.

# Arithmetic Operators.
print(2+2) # Addition (x = x + 3 / short: x += 3).
print(5-2) # Substraction (x = x - 3 / short: x -= 3).
print(5*2) # Multiplication (x = x * 3 / short: x *= 3).
print(6/2) # Division (x = x / 3 / short: x /= 3).
print(7 % 2) # Modulus (x = x % 3 / short: x %= 3).
print(2**3) # Exponentiation (x = x ** 3 / short: x **= 3).
print(7//2) # Floor division (x = x // 3 / short: x //= 3).
