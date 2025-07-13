
from random import choice, randint

print('\n\n')

#       Ejercicios 1

def list_of_hexa_colors():
    hex = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lst = [0, 0, 0, 0, 0, 0]

    for i in range(len(lst)):
        lst[i] = choice(hex)
    return '#' + ''.join(lst)

print(list_of_hexa_colors())


print()


#       Ejercicios 2

def list_of_rgb_colors():
    red, green, blue = 0, 0, 0
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return 'rgb(' + str(red) + ', ' + str(green) + ', ' + str(blue) + ')'

print(list_of_rgb_colors())

print('\n\n')


#       Ejercicios 3

text = str(input('¿hexa o rgb? = '))
num = int(input('¿Cuantos colores? = '))

def generate_color(text, num):
    lst = []
    if text == 'hexa':
        for i in range(num):
            lst.append(list_of_hexa_colors())
        print(lst)
    elif text == 'rgb':
        for i in range(num):
            lst.append(list_of_rgb_colors())
        print(lst)
    else:
        print('es necesario escoger unicamente entre hexa o rgb')

generate_color(text, num)

print()




