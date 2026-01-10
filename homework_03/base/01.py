"""
Написать функцию, которая принимает неограниченное количество чисел в виде позиционных аргументов и ключевой аргумент — операцию над этими числами (сложение или умножение).
Функция должна возвращать результат выполнения указанной операции.
"""

def numbers(*args, operation):
    if operation == '+':
        total = 0
        total = sum(args)
    elif operation == '*':
        total = 1
        for i in args:
            total *= i
    else:
        total = "Unsupported operation"
    print(f"Result: {total}")


numbers(1,2,3, operation='*')
