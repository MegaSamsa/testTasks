# Создать массив из 20 элементов в диапазоне (случайным образом) значений от -15 до 14 включительно. Определить количество элементов по модулю больших, чем максимальный.

import random

rnd_list = [random.randint(-15, 14) for _ in range(20)]
print(f"Входной массив: {rnd_list}")

max_el = max(rnd_list)
print(f"Наибольший элемент: {max_el}")

bigger_count = sum(1 for el in rnd_list if abs(el) > abs(max_el))

print(f"Количество элементов, больших по модулю, чем {max_el}: {bigger_count}")
