from sys import path

path.append("..\\packages")

from packages.todolist import enter, help, show, write

t = write.op()
while True:
    n = input('Input action: ')
    if n == 'enter':
        enter.enter(t)
    elif n == 'view':
        show.show(t)
    elif n == 'exit':
        write.wr(t)
        break
    elif n == 'help':
        help.help()

if __name__ == '__main__':
    print('I prefer to be a module')
else:
    print('I like to be a module')