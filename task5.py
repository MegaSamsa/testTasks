# Пользователь последовательно вводит с клавиатуры числа в консоль. Как только пользователь ввел «пустую строку» вывести на экран сумму введенных чисел и завершить работу программы.

num_sum = 0

while True:
    input_num = input("Введите число: ")

    if input_num != "":
        try:
            num_sum += int(input_num)
        except ValueError:
            print("Введённое значение не является числом. Попробуйте снова")
    else:
        print(f"Сумма введённых чисел: {num_sum}")
        break
