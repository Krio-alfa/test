# def INPUT(diction):
#     name = 'Default'
#     num = 1
#     while int(num) > 1 or int(num) < 15:
#         num = input('Number of task: ')  # Asking number.
#         if int(num) < 1 or int(num) > 15:
#             print('Input again(only from 1 to 15)')
#             num = 1
#             continue
#         else: 
#             name = input('Name: ')  # Asking name.
#             if len(name) < 7:
#                 print('Name have to be more than 7 sym')
#                 name = 'Default'
#                 continue
#             else: 
#                 if num in diction:
#                     diction[num] = name
#                 else:
#                     diction.update({str(num):name})
#                 break



# def VIEW(diction):
#     for i in diction:
#         print(diction[i])


# def HELP():
#     print('''
#     Name have to be more than 7 sym.
#     Priority have to be from 1 to 15.
#     Number of task have to be from 1 to 15.
#     'exit' for exit. 'enter' for entering task.
#     'view' for viewing all list. 'help' for this window.
#     ''')

# t = {}

# def main(n):
#     if n == 'enter':
#         INPUT(t)
#     elif n == 'view':
#         VIEW(t)
#     else:
#         HELP()

# if __name__ == '__main__':
#     print("Самостоятельныи модуль")
#     while True:
#         a = input('Input action: ')
#         if a == exit:
#             print('Thank for using')
#             break
#         else:
#             main(a)
# else:
#     print('Встраемый модуль')