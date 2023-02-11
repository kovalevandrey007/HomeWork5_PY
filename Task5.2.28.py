# 5.2[28]: Напишите рекурсивную функцию 
# sum(a, b), возвращающую сумму 
# двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(0,0) -> 0
# <function_name>(0,2) -> 2
# <function_name>(3,0) -> 3

def sum_(a, b):
    if b == 0:
        return a
    if a == 0:
        return b
    a += 1
    b -= 1
    return sum_(a, b)
a = int(input())
b = int(input())
print(sum_(a,b))