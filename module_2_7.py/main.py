def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(2, 4, 6)
print_params(a = 2, b = 3)
print_params(c = 5)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [7, True, 'stroka']
values_dict = {'a': 4, 'b': 5, 'c':6}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32 ,'Строка' ]
print_params(*values_list_2, 42)