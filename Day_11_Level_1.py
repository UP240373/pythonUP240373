
print('\n\n')

#       Ejercicios 1

def add_two_numbers(n1, n2):
    return n1 + n2

print(add_two_numbers(3, 4))

print()


#       Ejercicios 2

r = float(input('Introduce el radio del circulo: '))

def area_of_circle(r):
    return 3.1416 * r * r

print(area_of_circle(r))

print('\n\n')


#       Ejercicios 3

n1 = int(input('Introduce un numero: '))
n2 = float(input('Introduce otro numero: '))

def add_all_nums(n1, n2):
    n = int()
    if type(n1) == type(1) and type(n2) == type(1):
        return n1 + n2
    else:
        return 'Ingrese numeros integros'

print(add_all_nums(n1, n2))

print('\n\n')


#       Ejercicios 4

celsuis = float(input('Ingrese la temperatura en grados Celsuis: '))

def convert_celsius_to_fahrenheit(celsuis):
    return (celsuis * (9/5)) + 32

print('Temperatura en grados Fahrenheit:',convert_celsius_to_fahrenheit(celsuis))

print('\n\n')


#       Ejercicios 5

mouth = int(input('Ingresa un mes (1-12): '))

def check_season(mouth):
    if mouth < 1 or mouth > 12:
        return 'Numero invalido, ingrese otro porfavor'
    else:
        if mouth >= 10 and mouth <= 12: 
            season = 'Otoño'
        elif mouth >= 1 and mouth <= 3: 
            season = 'Invierno'
        elif mouth >= 4 and mouth <= 6: 
            season = 'Primavera'
        elif mouth >= 7 and mouth <= 9: 
            season = 'Verano'
        return season

print(check_season(mouth))

print('\n\n')


#       Ejercicios 6

x = float(input('Ingrese x para 4x + 5: '))

def calculate_slope(x):
        return (4 * x) + 5

print(calculate_slope(x))

print('\n\n')


#       Ejercicios 7

print('Ecuacion: ax^2 + bx + c')
a = float(input('Ingrese el valor de a: '))
b = float(input('Ingrese el valor de b: '))
c = float(input('Ingrese el valor de c: '))
x1 = 0
x2 = 0

def solve_quadratic_eqn(a, b, c):
        x1 = ((-b) - (((b * b) - (4 * a * c)) ** 0.5)) / (2 * a)
        x2 = ((-b) + (((b * b) - (4 * a * c)) ** 0.5)) / (2 * a)
        return x1, x2

print(f'Primer valor: {solve_quadratic_eqn(a, b, c)[0]}. Segundo valor: {solve_quadratic_eqn(a, b, c)[1]}')

print('\n\n')

#       Ejercicios 8

lst = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def print_list(lst):
    for i in lst:
        print(i)

print_list(lst)

print('\n\n')


#       Ejercicios 9

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def reverse_list(lst):
    lst = list(lst)
    lst.reverse()
    for i in lst:
        print(i)
    lst.reverse()

reverse_list(lst)

print('\n\n')


#       Ejercicios 10

lst = ['hola', 'como', 'estas', '?']

def capitalize_list_items(lst):
    for i in range(len(lst)): 
        text = str(lst[i])
        lst[i] = text.swapcase()
    return lst

print(capitalize_list_items(lst))

print('\n\n')


#       Ejercicios 11

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
text = int(input('Introduce el nuevo item: '))

def add_item(text):
    lst.append(text)
    return lst

print(add_item(text))

print('\n\n')


#       Ejercicios 12

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lst)
dele = int(input('Introduce el item que desea eliminar: '))

def remove_item(dele):
    check = dele in lst
    if check == True:
        lst.remove(dele)
        return lst
    else:
        return 'No existe el item dentro de la lista'

print(remove_item(dele))

print('\n\n')


#       Ejercicios 13

n = int(input('Introduce un numero: '))

def sum_of_numbers(n):
    result = int()
    for i in range(1, n + 1): 
        result += i
    return result

print(sum_of_numbers(n))

print('\n\n')


#       Ejercicios 14

n = int(input('Introduce un numero: '))

def sum_of_odds(n):
    result = int()
    for i in range(1, n + 1): 
        if i % 2 != 0:
            result += i
    return result

print(sum_of_odds(n))

print('\n\n')


#       Ejercicios 15

n = int(input('Introduce un numero: '))

def sum_of_even(n):
    result = int()
    for i in range(1, n + 1): 
        if i % 2 == 0:
            result += i
    return result

print(sum_of_even(n))

print('\n\n')


































































