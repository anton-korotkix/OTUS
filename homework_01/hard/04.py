"""
Задание 4: Римские числа
Пользователь вводит целое положительное число, программа должна вернуть строку в виде римского числа.

Примеры:
3   -> III
15  -> XV
234 -> CCXXXIV
"""

number = int(input("Input number: "))

rim = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
arab = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
startnumber = number
result = ""

ii=-abs(len(rim)+1) #инвертированная длина списка +1 т.к. границы range не входит

for i in range(-1,ii,-1):
    if (number//arab[i]) > 0:
        result += rim[i]*(number//arab[i]) #сколько i влезет в number - столько пишу римских
        number -= arab[i]*(number//arab[i]) #уменьшаю исходный number на вычисленное количество
        if number % arab[i] == 0: #если добрался до нуля - финиш
            break
            
print(f"{startnumber} -> {result}")
