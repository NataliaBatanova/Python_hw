# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Введите целое число: "))
sum = 0
while number != 0:
    sum = sum + number % 10
    number = number // 10
print("Сумма цифр Вашего числа равна: ", sum)