#1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params()
print_params(45)
print_params('река',45)
print_params([5, 6, 7],[1, 2, 3],[3, 3])
print_params(b=25)
print_params(c=[1, 2, 3])

# 2.Распаковка параметров:

values_list = [1, True,'Лес']
values_dict = {'a':'Дом', 'b':3.14, 'c':False}

print_params(*values_list)
print_params(**values_dict)

#3.Распаковка + отдельные параметры:

values_list_2 = [1.454, 'paint']
print_params(*values_list_2, 42)