# Написать функцию, которая определяет количество разрядов введенного целого числа.

def digit_calc(num):
    num = abs(num)

    if num != 0:
        i = 0
        while num > 0:
            num = num // 10
            i += 1
        return i
    else:
        return 1

try:
    input_num = int(input("Введите целое число: "))
    print(f"Количество разрядов числа {input_num}: {digit_calc(input_num)}")
except ValueError:
    print("Введённое значение не является целым числом")
