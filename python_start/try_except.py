'''try_except '''

#try_except - конструкция для обработки исключений
#
# исключение - проьлема в логике работы кода
# 
# ошибка  - проблема в синтанксисе кода (отсут второй кавычки, скобки, двоеточия и т.д. - неправильное написание кода) 

#ошибки: 

# for i in range(1, 10)
# print(i) - синтаксическая ошибка - SyntaxError (отсутствие : )

# for i in range(1, 10):
# print(i)   - IndentationError: expected an indented block (отсутствие отступа)

#TabError - ошибка табуляций 

# for i in range(1, 10):
#         print(i) - излищняя табуляция и прообел, но Пайтон сам поправляет 


#исключения: 

#print(10 / 0) - ZeroDivisionError: division by zero - ощибка деления на ноль 

# a = 10 
# b = 20 
# print(c) - NameError: name 'c' is not defined - исключение отсутствия имени 


# string = 'word'
# print(string.get(o)) - AttributeError у строк нет такого метода 


# dict_ = {'a':10, 'b':20}

# dict_['c']  # KeyError - вытаскиваем отсутствующий ключ


# list_ = [1, 2, 3]
# list_[4] IndexError: - отсутствие индекса в диапазоне 

# str_ = 'youtube'
# num1 = 12
# str_ + num1 TypeError - неотзя склеивать строку и числа  

# int(12)
# int(2.5)
# print(int('103'))
# print(int('aijaaa')) - ValueError - передан правильный тип данных, но не правильное значение 

# from math import sqrt 
# # print(sqrt(25))
# print(sqrt(-25))  ValueError - ошибка значения, когда тип объекта прлходит для совершения операции но значение не подходит


# print('Hello')
# print(10 / 0)
# print('world')


# try: 
#     print('Hello')
#     print(10 / 0)
#     print('world')
# except: 
#     print('что то пошло не так, Упсс')
# else: 
#     print('try обратал без ошибок')

# finally:     
#     print('я обработал в любом случае')

# try: 
#     попытка выполнить код, которая потенциально может вызвать исключение 
# except:
#     обработка исключения - сработает если в try есть исключение
# else: 
#     выполняется если try прощел без исключения 
# finally: 
#     выполняется в любом случае 


# try: 
#     print(c)
#  except Exception as error:
#     print(error)                   
# print('друнгой участок кода')

# a = {'a': 1, 'b': 2}
# try:
#     a['d']
# except KeyError: 
#     print('NO') #- вылавили ошибку 
# except ZeroDivisionError: 
#     print('NOOOO')    

#raise - оператор для генерации собсьвенных исключений

# raise название_исключения(описания исключения)

temp = int(input())
if temp > 100: 
    raise Expection (температура не может  быть выше 100 градусов)

print('jbv')
