# def enter_task(list):
#     prior = 1
#     name = 'Default'
#     num = 1
#     while num > 1 or num < 15:
#         num = input('Number of task: ')  # Asking number.
#         if num < 1 or num > 15:
#             print('Input again(only from 1 to 15)')
#             num = 1
#             continue

#     while len(name) > 7:
#         name = input('Name: ')  # Asking name.
#         if len(name) < 7:
#             print('Name have to be more than 7 sym')
#             name = 'Default'
#             continue

#     while prior > 1 or prior < 100:  # Asking priority.
#         prior = input('Priority: ')
#         if prior < 1 or prior > 100:
#             print('Input again(only from 1 to 15)')
#             prior = 1
#             continue
    
#     result = '№'+ str(num),'|',name,'|',str(prior)  # Creating result line.
#     list.append(result)

# def display_task_list(list):
#     for t in list:
#         print(t)

# def cond_display():  # Instuctions
#     print('''
#     Name have to be more than 7 sym.
#     Priority have to be from 1 to 15.
#     Number of task have to be from 1 to 15.
#     'exit' for exit. 'enter' for entering task.
#     'view' for viewing all list. 'help' for this window.
#     ''')

# tasking = []

# def main(n):  # Asking for action
#     if n == 'enter':
#         enter_task(tasking)
#     elif n == 'view':
#         display_task_list(tasking)
#     else:
#         cond_display()

# if __name__ == '__main__':  # Checking __main__
#     print("Самостоятельныи модуль")
#     while True:
#         a = input('Input action')
#         if a == exit:
#             print('Thank for using')
#             break
#         else:
#             main(a)
# else:
#     print('Встраемый модуль')