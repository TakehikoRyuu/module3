# Дополнительное практическое задание по модулю
def calculate_structure_sum(*data):
    sum = 0
    for item in data:
        if isinstance(item, int):
            sum += item
        elif isinstance(item, str):
            sum += len(item)
        elif isinstance(item, dict):
            sum += calculate_structure_sum(*item.keys())
            sum += calculate_structure_sum(*item.values())
        elif isinstance(item, list) or isinstance(item, set) or isinstance(item, tuple):
            sum += calculate_structure_sum(*item)
    return sum

data_structure = [
  [1, 2, 3], # <class 'list'>
  {'a': 4, 'b': 5}, # <class 'dict'>
  (6, {'cube': 7, 'drum': 8}), # <class 'tuple'>
  "Hello", # <class 'str'>
  ((), [{(2, 'Urban', ('Urban2', 35))}]) # <class 'tuple'>
]

result = calculate_structure_sum(data_structure)
print(result)