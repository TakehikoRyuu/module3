# Распаковка позиционных параметров
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params() # 1 строка True
print_params(b = 25) # 1 25 True
print_params(c = [1,2,3]) # 1 строка [1, 2, 3]

values_list = (9, 'Да', True)
print_params(*values_list) # 9 Да True
values_dict = {'a': 11, 'b': 'Надо', 'c': False}
print_params(*values_dict) # 11 Надо False

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42) # 54.32 Строка 42