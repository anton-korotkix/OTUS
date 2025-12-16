"""
Классическая игра FizzBuzz. Программа в цикле выводит в консоль числа от 1 до 100.
Если число кратно 3, вместо него выводится Fizz.
Если кратно 5 — Buzz.
Если кратно и 3, и 5 — FizzBuzz.
"""

for i in range(1,101):
    if int(i) % 3 == 0 and int(i) % 5 == 0:
        string = "FizzBuzz"
    elif int(i) % 5 == 0:
        string = "Buzz"
    elif int(i) % 3 == 0:
        string = "Fizz"
    else:
        string = ""
    print(f"{i} - {string}")
