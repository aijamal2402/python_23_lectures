'''множества (set)'''
#множества - изменяемый не упорядоченный тип данных/ содержит в себе уникальные элементы и только неизменяемые типы  данных/

#a = {}
#print(type(a)) # dict 

#b = set()
#print(type(b)) # set 

#c = {'a', 1, True, (1, 2), 2.54, None}

#e = {1, 2, ['a', 'b']} #TypeError

#d = {1, 2, (1, 2 ['a', 'b'])} #TypeError

#list_ = [1, 2, 3, 3, 3, 3]
#a = set(list_)
#print(a) # удалили дубликаты

"""  
Создайте словарь, ключами которого являются буквы английского алфавита, а значениями – 
соответствующие им порядковые номера в алфавите. Для удобства можете воспользоваться модулем string
"""

# from string import ascii_lowercase 
# a = {}
# num = 1
# for i in ascii_lowercase:
#     a[i] = num 
#     num += 1
# print(a)      


# print(ord('a')) # порядковый номер возвращает 
# print(chr(97)) # 

# a = {}
# num = 1
# for i in a:
#     a[i] = num 
#     num = ord(i)
# print(a)      

# a = {}
# for i in range(26):
#     a [chr(i + ord('a'))] = i + 1
# print(a)    


emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
       'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
       'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
       'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
       'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
       'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}
for k, v in emails.items(): 
    # print(k)
    # print(v)
    for name in v:
        print(name + '@' + k)   

#print(emails)       



 
