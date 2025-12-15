"""
Пользователь вводит через консоль 10 чисел. Программа должна определить максимальное число и вывести его в консоль.
"""
i = 0
max = 0
string = ""
numbstring = ""


while i != 10:
    dig = input("\nInput number: ")
    string += dig + " "
    if dig.isdigit():
        if int(dig) > int(max):
            numbstring += dig + " "
            max = dig
        i += 1
    else:
        continue
else:
    print(f"Full string: {string}\nNumber string: {numbstring}\nMax: {max}")
