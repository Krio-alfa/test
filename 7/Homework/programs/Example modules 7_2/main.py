from sys import path

path.append("..\\packages")

from packages.summa.plus_mod import plus

a = 100
b = 80

print(plus(a,b))

if __name__ == '__main__':
    print('I prefer to be a module')
else:
    print('I like to be a module')