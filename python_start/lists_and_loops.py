""" списки и циклы """

# list()
# Список - изменяемый, упорядоченный, индексируемый, итерируемый тип данных. Нужен для хранения нескольких элементов

# Элементами списка могут быть любые типы данных

# list_ = [1, 'string', True, False, [1, 2], None, {'a': 12}, {1, 2}, ('a', 'b', 'c')]
# print(list_)


list1 = [1, 2, 3, 4, 5, [6, 7]]
        #0  1  2  3  4    5
list1[0] # 1
list1[1] # 2
list1[2] # 3
list1[5] # [6, 7]
list1[5][0] # 6
list1[-1] # [6, 7]

list1[1:-2:] # [2, 3, 4]


""" добавление элементов в список """

a = [1, 2, 3]

# a.append(element) - добавляет элемент в конец списка
# print('До ', a)
# a.append(4)
# a.append(5)
# a.append(6)
# print('После ', a)

# a.insert(index, element) - вставляет элемент на место указанного индекса
# print('До', a)
# a.insert(1, 'hello')
# print('После', a)

# a.append(element) -> a.insert(len(a), element)

# a.insert(1234, 'world') # добавил в конец [1, 2, 3, 'world']


# list1.extend(list2) - добавляет все элементы list2 в list1

# my_list1 = [4, 2, 6]
# my_list2 = [1, 3, 8]

# my_list1.append(my_list2)
# print(my_list1) # [4, 2, 6 ,[1, 3, 8]]

# my_list1.extend(my_list2)
# print(my_list1) # [4, 2, 6, 1, 3, 8]

# new_list = my_list1 + my_list2
# print(my_list1) # [4, 2, 6]
# print(new_list) # [4, 2, 6, 1, 3, 8]

""" замена элементов """
# b = ['a', 'b', 'c', 'd']
# b[2] # 'c'
# b[2] = 'g'
# print(b) # ['a', 'b', 'g', 'd']


""" удаление элементов """

ab = ['a', 'b', 'c', 'd']

# ab.pop([index]) - удаляет элемент по указанному индексу, если индекс не указан - удаляет последний элемент. Возвращает удаленный элемент

# ab.pop(1)
# print(ab) # ['a', 'c', 'd']

# ab.pop()
# print(ab) # ['a', 'b', 'c']

# deleted_el = ab.pop(2)
# print(deleted_el) # 'c'
# print(ab) # ['a', 'b', 'd']
# ab.append(deleted_el) # ['a', 'b', 'd', 'c']


# list3.remove(значение) - удаляет первый встретившийся элемент с указанным значением

# list3 = ['Azamat', 'Kolya', 'Adilet', 'Azamat']
# list3.remove('Azamat')
# print(list3) # ['Kolya', 'Adilet', 'Azamat']
# list3.remove(20) # ValueError


# ab.clear() - полностью очищает список
# ab.clear()
# print(ab) # []

# del element
# del ab
# print(ab)

# del ab[3]
# print(ab) # ['a', 'b', 'c']

# del ab[:2]
# print(ab) # ['c', 'd']


# a1 = [1, 2, 3]
# b2 = a1

# b2.append(4)
# print(b2) # [1, 2, 3, 4]
# print(a1) # [1, 2, 3, 4]
# print(b2 is a1) # True


""" копирование списка """
# a3 = [1, 2, 3]
# a4 = a3.copy()
# a5 = a3[:]


""" сортировка списка """

# num_list = [4, 3, 8, 5]
# num_list.sort()
# print(num_list) # [3, 4, 5, 8]

# num_list.sort(reverse=True)
# print(num_list) # [8, 5, 4, 3]

# str_list = ['b', 'c', 'e', 'a', 'd']
# str_list.sort()
# print(str_list) # ['a', 'b', 'c', 'd', 'e']


# name_list = ['Azamat', 'Ivan', 'Zeynep', 'Aliya']
# name_list.sort(key=len)
# print(name_list) # ['Ivan', 'Aliya', 'Azamat', 'Zeynep']

# name_list = ['Azamat', 'Ivan', 'Zeynep', 'Aliya']
# new_list = sorted(name_list, key=len, reverse=True)
# print(name_list) # ['Azamat', 'Ivan', 'Zeynep', 'Aliya']
# print(new_list) # ['Azamat', 'Zeynep', 'Aliya', 'Ivan']

# my_list = ['a', 'b', 'c', 'd', 'e']
# my_list.reverse()
# print(my_list) # ['e', 'd', 'c', 'b', 'a']

# new_list = my_list[::-1] 
# print(new_list) # ['e', 'd', 'c', 'b', 'a']