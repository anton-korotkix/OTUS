"""
Пользователь вводит строку, содержащую любые символы (буквы, цифры и специальные символы). Программа должна вычислить и вывести сумму всех цифр, присутствующих в этой строке.
"""

string = input("Input string: ")
sum = 0

for symbol in string:
    if symbol.isdigit():
        sum += int(symbol)
    else:
        continue
print(f"String: {string}\nTotal sum: {sum}")
