def calculate_structure_sum(*args):
    total_sum = 0

    for data in args:
        if isinstance(data, (list, tuple, set)):
            total_sum += calculate_structure_sum(*data)  # Распаковываем элементы и передаем их рекурсивно
        elif isinstance(data, dict):
            total_sum += calculate_structure_sum(*data.keys(), *data.values())  # Обрабатываем ключи и значения
        elif isinstance(data, int):
            total_sum += data
        elif isinstance(data, str):
            total_sum += len(data)

    return total_sum

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

sum_of_numbers_and_lengths = calculate_structure_sum(data_structure)
print(f"Сумма чисел и длин строк: {sum_of_numbers_and_lengths}")
