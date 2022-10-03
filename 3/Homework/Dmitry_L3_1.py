# # Home work 3.1
# hat_list = [1, 2, 3, 4, 5]

# red_list = hat_list[:] # New list.
# a = input('Enter a number with that i will replace the middle number in the list:')
# i = len(hat_list) / 2 # Calculating center.
# red_list[i] = a

# red_list.remove(-1) # Deleting last index with number.

# print('hat:'+len(hat_list),'\n','redacted:'+len(red_list))

# # Home work 3.2
# beatles = []
# print('Step 1:', beatles)
# beatles.append('John Lennon', 'Paul McCartney', 'George Harrison') # Adding some names.
# print('Step 2:', beatles)
# for i in range(2):
#     beatles.append(input('Input name:')) # Asking names from user two times.
# print('Step 3:', beatles)
# del beatles[-1:-2] # Deleting last two.
# print('Step 4:', beatles)
# beatles.insert(0,'Ringo Starr') # Inserting to 0 index.
# print('Step 5:', beatles)

# # Home work 3.3
# n = int(input('How many numbers:'))
# lst = [0 for i in range(n)]
# a = int((input("Reversed - 1 or 0 - not reversed:")))
# for i in range(n):
#     lst[i] = float(input('Number:'))
# swap = True # Just to enter the loop.

# if a == 0:    
#     while swap: # Increased.
#         swap = False # To stop at the right moment.
#         for i in range(len(lst) - 1):
#             if lst[i] > lst[i+1]:
#                 swap = True # Swap happend.
#                 lst[i], lst[i+1] = lst[i+1], lst[i]
# else:
#     while swap: # Reversed.
#         swap = False # To stop at the right moment.
#         for i in range(len(lst) - 1):
#             if lst[i] < lst[i+1]:
#                 swap = True # Swap happend.
#                 lst[i], lst[i+1] = lst[i+1], lst[i]
# print(lst)

# # Home work 3.4
# my_list = [1, 2, 4, 4, 1, 4 ,2, 6, 2, 9]
# res_list = []
# my_list.sort()
# for i in range(len(my_list)):
#     if my_list[i] not in res_list:#Cheking numbers in res list if they already there just skip.
#         res_list.append(my_list[i])
#     else:
#         pass

# print(res_list)