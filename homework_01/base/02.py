"""
Пользователь вводит строку через консоль (состоящую только из букв в разном регистре). Программа должна создать новую строку, содержащую только те буквы из исходной строки, которые были в верхнем регистре.
"""

string = input("Input string (only letters): ")
result = ""

if any(symbol.isdigit() for symbol in string):
    print("Error: numbers in string")
else:
    for symbol in string:
        if symbol.isupper():
            result += symbol
        else:
            continue
    if result == "":
        print("No UPPERcase symbols in string")
    else:
        print(f"Old string: {string}\nNew string with only UPPERcase: {result}")
