'''scopes_ - области видимости и пространства имен'''

'''LEGB - '''
# Local - локальная 
# enclosed - замкнутая 
# Global - глобальная 
# built-in - встроенная 

# '''Область видимости''' - часть программы, где будет доступно 
# то или иное имы (переменная, функция, класс и т.д)


# name = 'Janat'
# name = 'Akbar'
# print(name) # Akbar

# name = 'Marina' #global пространство 
# def func():
#     name = 'Nikolay'
# print(name)    # Marina 

# def func2():
#     print(name)  # local пространство 
# func2()    #Marina

# def func3():
#     a = 10 

# print(a)    # NameError:

'''имена из локальной области недоступны в глоальной области, 
но в локальной области доступны имена из глобальной области!'''


# for i in range(1, 10):
#     res = i * 2 
# print(res)    # 18

# number = 20 
# if number % 2 == 0:
#     res2 = 35 
# print(res2)    # табуляция не влияет на области видимости 

# num = 10 

# def func():
#     global num  # функция чтобы локальный превратить в глобальный 
#     num = 50 

# func()
# print(num)   


# x = 20 # global 

# def func_outer():
#     x = 15  # non local
#     def func_inner():
#         x = 25 # local 
#         print(x)
#     func_inner()

# func_outer()    # 25

# number = 20 
# def outer_func():
#     # nonlocal
#     number = 19   # 19 
#     print(number)
#     def inner_func():
#         nonlocal number     # поменять  
#         number = 25  # 25 
#         print(number)
#     inner_func()
#     print(number)    # 19 

# outer_func()     


'''globals(), locals()'''

a = 20 
# print(globals()) # словарь из встроенных имен 
# globals() - показывает имена на глобальном уровне видимости

# print(locals()): 
# def my_func():
#     var = 95 
#     tel = 100
#     print(locals())
# my_func()         #{'var': 95, 'tel': 100}


# locals() - показывает доступные имена той области в которой была вызвана  


def get_drade(mark):
    mark = 1
    if grade > 87:
        grade = 5
    return grade
    
get_grade(85)        

