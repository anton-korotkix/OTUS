"""
Написать функцию, которая принимает неограниченное количество чисел в виде позиционных аргументов и ключевой аргумент — операцию над этими числами (сложение или умножение).
Функция должна возвращать результат выполнения указанной операции.
"""

def numbers(*args, operation):
    if operation == '+':
        total = sum(args)
    elif operation == '*':
        total = 1
        for i in args:
            total *= i
    else:
        total = "Unsupported operation"
    return total

numbers(1,4,10, operation='*')
