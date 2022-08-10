# '''функции'''

# # print()
# # max()
# # pow()

# # функции - именнованный блок кода, который принимает какие либо значения, 
# # совершает над ними определенные действия и возвращает результат этих действий

# # a1 = 100 
# # (a1 ** 2) / 10 * 15 
# # a2 = 200
# # (a2 ** 2) / 10 * 15 
# # a3 = 300
# # (a1 ** 2) / 10 * 15 
# # a4 = 400
# # (a1 ** 2) / 10 * 15 

# # DRY() - Don`t repeat yourself - не повторяйся - принцип написания кода

# # def aija(): 
# #     print('Hello world')

# # aija() - вызвали ее     

# # def my_sqr(num):
# #     print((num ** 2) / 10 * 15)

# # a = my_sqr(100)           #15000.0
# # a + 500 #TypeError:
# # my_sqr(200) 
# # my_sqr(300)
# # my_sqr(400)  

# # def aija(num):
# #     return(num ** 2) / 10 * 15

# # b = aija(100)
# # print(b)            # 15000.0

# # print(b + 15500)     # 30500.0


# a = print()
# print(a)    #None

# def имя функции(параметры):
#     тело_функции

# имя_функции(аргументы)

# параметры - это значения для функции при вызове

# return - ключевое слово для возвращения результата выполнения функции   


# def add(x: int, y: int):
#     """написать комментарий - принимает 2 числа и складывает их между собой""" 
#     num = x + y
#     return num  # после него ничего не читается 

# ptint(add())    


# параметры бывают 2 типов: 
# 1. обязательные (с)
# 2. необязательные (по умолчанию) (с=10)

# def sub(x, y):
#     res = x - y 
#     return res

# a = sub(10, 40)  
# print(a)

# def sub(x, y=5):
#     res = x - y 
#     return res

# b = sub(10)  
# print(b)

# def func(x = 5, y): - # SyntaxError: сначало указывается обязательная

# def func(a, b, c, d, e=10, f=20):
#     pass # заглушка, чтобы ничего не происходило 


# аргументы бывают: 
# 1. именнованные
# 2. позиционные  

# def my_func(num1, num2, num3=10):
#     return num1 + num2 + num3

# #     позиционные  

# my_func(10, 20, 30) # 65 
# my_func(50, 60) # 120

# #   именнованные
# my_func(num1 = 5, num2 = 10, num3 = 15)
# my_func(num3 = 15, num1 = 5, num2 = 10) # место не имеет значения, будет выполняться - удобно 


## смешанный: именнованный, позиционный 

# my_func(10, 5, num3=10)  # 25

# def send_message(email, message):
#     return f'{message} было отправлено на {email}'

# def notify_user(name):
#     message = input('введите сообщение')
#     email = input('введите почту')
#     note = send_message(email, message)
#     print(f'здравствуйте {name}. {note}') 

# notify_user('Айжамал')  


# *args - кортеж позиционных аргументов 
# **kwargs - словарь именнованных аргументов (keyword arguments)  

# def func(*args, **kwargs):  # неважно их наименование, главное звездочки 
#     print(args, 'args')
#     print(kwargs, 'kwargs')

# # func(1, 2, 3)    
# # func(a = 1, b = 2, c = 3)  
# func(1, 2, 3, a = 1, b = 2, c = 3) # (1, 2, 3) args {'a': 1, 'b': 2, 'c': 3} kwargs

# def my_func(*args): 
#     counter = 0 
#     for i in args: 
#         counter += i 
#     return counter   

# print(my_func(1, 2, 3, 4, 5, 6, 7))     # 28 = сложение всх чисел 


# def func(a, b, c):
#     return a + b + c

# nums = (3, 4, 8)
# dict_ = {'a': 10, 'b': 20, 'c': 40}
# print(func(*nums)) # 15
# print(func(**dict_))    # 70


def func():
    yield 1
    yield 2
    yield 3
    yield 4

print(list(func()))    
