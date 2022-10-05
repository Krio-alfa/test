# # Home work 5.1
# def l_y(year):
#     if year % 4 != 0 or year % 100 !=0 or year % 400 == 0: # Checking.
#         return True
#     elif year % 4 == 0 or year % 100 ==0 or year % 400 != 0:
#         return False
#     else:
#         return None

# test_data = [1900,2000,2016,1987] # Testing.
# test_res = [False, True, True, True]
# for i in range(len(test_data)):
#     yr = test_data[i]
#     print(yr,"->",end="")
#     res = l_y(yr)
#     if res == test_res[i]:
#         print('OK')
#     else:
#         print('Failed')

# # Home work 5.2
# def liters_100km_to_miles_gallon(lit):
#     gallon = lit / 3.7855411784
#     mile = 100000 / 1609.344
#     return gallon,mile

# def miles_gallon_to_liters_100km(gallon):
#     lit = gallon * 3.7855411784
#     return lit

# # Home work 5.3
# def factorial(n):
#     if n < 0: return None
#     if n < 2: return 1
#     t=1
#     v=0
#     res = n - 1
#     while t != 10:
#         ls = [1,1,2]
#         for i in ls:
#             v*=i
#         ls.append(v)
#         v = 0
#     return ls[res]

# print(factorial(6))

# # Home work 5.4
# def febo(n):
#     if n < 1: return None
#     if n < 3: return 1
#     ls = [1,1,2]
#     for i in range(n + 10):
#         t = ls[i - 1]+ls[i]
#         ls.append(t)
#     return ls[n - 1]
