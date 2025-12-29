"""
Написать программу, которая удаляет из списка все дубликаты, сохранив исходный порядок элементов.
"""

string = input("Input string: ")
result = list()

for item in string.split(): #иду по каждому элементу списка подстрок исходной строки
    if item not in result:  #если такого элемента нет в готовом списке - добавляю
        result.append(item) 

print(f"{string} -> {result}")
