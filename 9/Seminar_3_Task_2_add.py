"""Задайте последовательность чисел. Напишите программу, которая выведет
список неповторяющихся элементов исходной последовательности."""
def my_set_func(user_str):

    #user_str = '4 5 6 7 7 8 9 10 3 4 6 21'
    user_list = user_str.split()
    namber_list = []
    for i in user_list:
        try:
            x = int(i)
        except ValueError:
            x = 0
        else:
            namber_list.append(x)
    #print(set(namber_list))
    return set(namber_list)
