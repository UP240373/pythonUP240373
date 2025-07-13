
from random import choice, randint

print('\n\n')

#       Ejercicios 1

def random_user_id():
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lst = [0, 0, 0, 0, 0, 0]

    for i in range(len(lst)):
        lst[i] = choice(abc)
    return ''.join(lst)

print(random_user_id())


print()


#       Ejercicios 2

rango = int(input('Extension de la cadena: '))
num_codigos = int(input('Cuantos codigos se desea: '))

def user_id_gen_by_user(rango, num_codigos):
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    dct = {}
    lst = []

    for j in range(num_codigos):
        for i in range(rango):
            lst.append(0)
    
        for i in range(len(lst)):
            lst[i] = choice(abc)
        dct[j] = lst
        lst = []

    for j, i in dct.items():
        print(''.join(i))

user_id_gen_by_user(rango, num_codigos)

print()


#       Ejercicios 3

def rgb_color_gen():
    red, green, blue = 0, 0, 0
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)

    print('rgb', end='')
    return red, green, blue

print(rgb_color_gen())

print()




