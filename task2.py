# С клавиатуры вводится натуральное число. Найти его наибольшую цифру.

try:
    input_num = int(input("Введите натуральное число: "))
    if input_num > 0:
        input_num = str(input_num)
        max_num = max(input_num)
        print(f"Наибольшая цифра: {max_num}")
    else:
        print("Введённое число не является натуральным")
except ValueError:
    print("Введённое значение не является числом")
