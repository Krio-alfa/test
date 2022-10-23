Types_for_operation = [int, float]
a = 10
b = ''
print(type(a) in Types_for_operation)
print(type(b) in Types_for_operation)

try:
    value = int(input('Enter a natural number: '))
    print('the reciprocal of', value, 'is', 1/value)
except ValueError:
    print('I do not know what to do.')
except ZeroDivisionError:
    print('Division by zero is not allowed.')
except:
    print('Something strange has happened here... Sorry!')


while True:
    try:
        number = int(input('Enter a integer number: '))
        print(number/2)
        break
    except:
        print('Warning: the value entered is not a valid number. Try again...')