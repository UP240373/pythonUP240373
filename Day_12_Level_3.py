
from random import choice

print('\n\n')

#       Ejercicios 1

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def shuffle_list(lst):
    lst = list(lst)
    new_lst = list()

    for i in range(len(lst)):
        new_lst.append(choice(lst))
        lst.remove(new_lst[-1])
    return new_lst

print(shuffle_list(lst))

print()


#       Ejercicios 2

def randoms_array():
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random_lst = list()

    for i in range(7):
        random_lst.append(choice(lst))
        lst.remove(random_lst[-1])
    return random_lst

print(randoms_array())

print('\n\n')


