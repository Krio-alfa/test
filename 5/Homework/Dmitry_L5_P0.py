# # Home work 5.0
# def plus(a=0,b=0):
#     print('Result:',a+b)

# def minus(a=0,b=0):
#     print('Result:',a-b)

# def de(a=0,b=0):
#     print('Result:',a/b)

# def ad(a=0,b=0):
#     print('Result:',a*b)

# def pro(a=0,b=0):
#     print('Result:',a%b)

# def ostatok(a=0,b=0):
#     print('Result:',a//b)

# def mult(a=0,b=0):
#     print('Result:',a**b)

# def odd(a=0,b=0):
#     if(a % 2 == 0):
#         print('Result: '+a+' is odd')
#     else:
#         print('Result: '+a+' is even')
    
#     if(b % 2 == 0):
#         print('Result: '+b+' is odd')
#     else:
#         print('Result: '+a+' is even')

# def t(a=0,b=0):
#     print(type(a)+','+type(b))

# def avg(a=0,b=0):
#     print('Result:',(a+b)/2)

# def man(a=0,b=0):
#     if(a>b):
#         print(a+'is max',b+'is min')
#     elif(b<a):
#         print(b+'is max',a+'is min')
#     else:
#         print('There are equal')

# while True:
#     num1,op,num2 = input('Input numbers and operator(like this 5|\|7 or 0|exit|0): ').split("|")
#     num1,num2 = float(num1),float(num2)
#     if op == '-':
#         minus(num1,num2)
#     elif op == '+':
#         sum(num1,num2)
#     elif op == '/':
#         de(num1,num2)
#     elif op == '*':
#         ad(num1,num2)
#     elif op == '%':
#         pro(num1,num2)
#     elif op == '//':
#         ostatok(num1,num2)
#     elif op == '**':
#         mult(num1,num2)
#     elif op == 'type':
#         t(num1,num2)
#     elif op == 'avg':
#         avg(num1,num2)
#     elif op == 'max/min':
#         man(num1,num2)
#     elif op == 'odd/even':
#         odd(num1,num2)
#     else:
#         break
