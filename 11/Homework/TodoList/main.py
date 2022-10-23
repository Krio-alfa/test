from imports import *
from time import sleep as s
list = Task('todolist.txt')

program_work = True

while program_work:
    print()
    operation = input('Input operation(or anything fo help):')
    try:
        if operation == 'Add task':
            list.add()
        elif operation == 'Show task':
            list.show()
        elif operation == 'Change task':
            list.change()
        elif operation == 'Check task':
            list.check()
        elif operation == 'Save':
            list.save_file()
        elif operation == 'Show all':
            list.see_all()
        elif operation == 'Delete all':
            list.deleting_all()
        elif operation == 'Dzen':
            Dzen()
            s(5)
        elif operation == 'exit':
            program_work = False
        else:
            help()
            s(5)
    except:
        print('\n\n\nBe careful of what you printing')
    print()
