# Цель: научиться обращаться к функциям, как к объекту и передавать их в другие функции для вызова.

def apply_all_func(int_list, *functions):
    results = {}  # Создаем пустой словарь, куда будем выводить результат
    if all(isinstance(x, (int, float)) for x in int_list): # Проверяем что в листе только числа
        for i in range(len(functions)):  # Осуществляем перебор по количеству переданных функций
            #name = functions[i].__name__ # Передаем в переменную имя функций
            #z = functions[i](int_list) # результат работы функции
            #results[name] = z
            results[functions[i].__name__] = functions[i](int_list)
    else:
        raise ValueError("Аргументы являются не только числами")
    return results


#fun1 = apply_all_func([6, 20, 15, 9], len, sum, sorted)
try:
    print(apply_all_func([6, 20, 15, 9], max, min))
except ValueError as exc:
    print(exc)
try:
    print(apply_all_func([6, '20', 15, 9], len, sum, sorted))
except ValueError as exc:
    print(exc)
try:
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
except ValueError as exc:
    print(exc)
