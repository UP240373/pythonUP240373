
print('\n\n')

#       Ejercicios 1

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
lst = [i for i in numbers if i <= 0]

print(lst)

print()


#       Ejercicios 2

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lst = [i for columnas in list_of_lists for columnas1 in columnas for i in columnas1]

print(lst)

print()


#       Ejercicios 3

lst = [(i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]

print(lst)

print()


#       Ejercicios 4

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

lst = [[pais.upper(), pais[:3].upper(), capital.upper()] for [(pais, capital)] in countries]

print(lst)

print()


#       Ejercicios 5

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

lst = [{'country': pais.upper(), 'city': capital.upper()} for [(pais, capital)] in countries]

print(lst)

print()


#       Ejercicios 6

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
lst = [str(nombre + ' ' + apellido) for i in names for [nombre, apellido] in i]

print(lst)

print()


#       Ejercicios 7

pendiente = lambda x: (2 * x) + 15

x = int(input('Escoge un valor para x (f(x) = 2x + 15): '))

print('y =' , pendiente(x))

print('\n\n')


