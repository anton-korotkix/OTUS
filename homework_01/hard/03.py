"""
Задание 3: Плитка шоколада
Пользователь вводит длину и ширину плитки шоколада, а также размер куска, который хочет отломить. Программа должна вычислить - можно ли совершить подобный разлом или нет, если учесть, что ломать можно только по прямой.

Примеры:
3, 4, 6  -> True
5, 7, 8  -> False
4, 5, 12 -> True
"""

while length == "":
    length = int(input("Input length: "))
while width == "":
    width = int(input("Input width: "))
while piece == "":
    piece = int(input("Input piece size: "))

if piece > (length*width):
    print("Error: Piece size bigger than chocolate")

if piece % length == 0 or piece % width == 0:
    result = "True"
else:
    result = "False"

print (f"{length}, {width}, {piece} -> {result}")
