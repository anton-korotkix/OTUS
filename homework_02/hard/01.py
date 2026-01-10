"""
Задание 1: Получение однозначного числа
Пользователь вводит целое число, программа складывает все цифры числа, с полученным числом — то же самое, и так до тех пор, пока не получится однозначное число.

Примеры:
545   -> 5
12345 -> 6
"""

string = input("Input number: ")
inp_string = string
result = 0

def sumToOneDigit(s):
    summ = 0
    for i in range(0, len(s)): #перебор посимвольно
        summ+=int(s[i]) #суммирование
    return summ

if any(symbol.isdigit() for symbol in string): #проверяю все ли символы в строке являются цифрами
    result = sumToOneDigit(string)
else:
    print("Error: not number")
    
print(f"{inp_string} -> {result}") 
