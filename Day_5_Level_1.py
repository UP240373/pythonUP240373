
print('\n\n')

#       Ejercicios 1

lst = list()


#       Ejercicios 2

materia = ['Programacion', 'Calculo', 'Probabilidad', 'Ingles', 'Sistemas']
print(materia)

print("")


#       Ejercicios 3

print(len(materia))

print('\n\n')


#       Ejercicios 4

print(materia[0])
print(materia[2])
print(materia[4])

print('\n\n')


#       Ejercicios 5

mixed_data_types = ['Abdul', 18, 85, True, 'Aguascalientes, Ags']


#       Ejercicios 6

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']


#       Ejercicios 7

print(it_companies)
print("")


#       Ejercicios 8

print(len(it_companies))
print("")


#       Ejercicios 9

print(it_companies[0])
print(it_companies[3])
print(it_companies[6])

print('\n\n')


#       Ejercicios 10

it_companies[3] = 'Samsung'
print(it_companies)

print('\n\n')


#       Ejercicios 11

it_companies.append('it')
print(it_companies)

print('\n\n')


#       Ejercicios 12

it_companies.insert(4, 'it')
print(it_companies)

print('\n\n')


#       Ejercicios 13

it_companies = ['Facebook', 'Google', 'Microsoft', 'Samsung', 'IBM', 'Oracle', 'Amazon']

it_companies[0] = 'FACEBOOK'
it_companies[1] = 'GOOGLE'
it_companies[2] = 'MICROSOFT'
it_companies[3] = 'SAMSUNG'
it_companies[5] = 'ORACLE'
it_companies[6] = 'AMAZON'
print(it_companies)

print('\n\n')


#       Ejercicios 14

text1 = '#; '.join(it_companies)
print(text1)

print('\n\n')


#       Ejercicios 15

it_companies = ['Facebook', 'Google', 'Microsoft', 'Samsung', 'IBM', 'Oracle', 'Amazon']

does_exit = 'Facebook' in it_companies
print('¿Existe \"Facebook\" en la lista? =', does_exit)
does_exit = 'Google' in it_companies
print('¿Existe \"Google\" en la lista? =', does_exit)
does_exit = 'samsung' in it_companies
print('¿Existe \"samsung\" en la lista? =', does_exit)

print('\n\n')


#       Ejercicios 16

it_companies.sort()
print(it_companies)

print('\n\n')


#       Ejercicios 17

it_companies.sort(reverse=True)
print(it_companies)

print('\n\n')


#       Ejercicios 18

it_companies = ['Facebook', 'Google', 'Microsoft', 'Samsung', 'IBM', 'Oracle', 'Amazon']

it_companies.pop(0)
it_companies.pop(0)
it_companies.pop(0)
print(it_companies)
print("")


#       Ejercicios 19

it_companies = ['Facebook', 'Google', 'Microsoft', 'IT', 'IBM', 'Oracle', 'Amazon', 'IT']

it_companies.pop(7)
it_companies.pop(6)
it_companies.pop(5)
print(it_companies)
print("")


#       Ejercicios 20

it_companies = ['IT', 'Facebook', 'Google', 'Microsoft', 'IT', 'IBM', 'Oracle', 'Amazon', 'IT']

it_companies.pop(4)
print(it_companies)
print("")


#       Ejercicios 21

it_companies = ['IT', 'Facebook', 'Google', 'Microsoft', 'IT', 'IBM', 'Oracle', 'Amazon', 'IT']

it_companies.remove('IT')
print(it_companies)
print("")


#       Ejercicios 22

it_companies = ['IT', 'Facebook', 'Google', 'Microsoft', 'IT', 'IBM', 'Oracle', 'Amazon', 'IT']

it_companies.pop(4)
print(it_companies)
print("")


#       Ejercicios 23

it_companies = ['IT', 'Facebook', 'Google', 'Microsoft', 'IT', 'IBM', 'Oracle', 'Amazon', 'IT']

it_companies.pop()
print(it_companies)

print('\n\n')


#       Ejercicios 24

it_companies = ['IT', 'Facebook', 'Google', 'Microsoft', 'IT', 'IBM', 'Oracle', 'Amazon', 'IT']

it_companies.remove('IT')
print('Existe \"IT\" en la cadena:', 'IT' in it_companies)
it_companies.remove('IT')
it_companies.remove('IT')
print('Existe \"IT\" en la cadena:', 'IT' in it_companies)
print(it_companies)
print("")


#       Ejercicios 25

it_companies.clear()
print(it_companies)
print('\n\n')


#       Ejercicios 26

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

print(' '.join(front_end))
print(' '.join(back_end))

print("")


#       Ejercicios 27

full_stack = (' '.join(front_end)) + (' ')+ (' '.join(back_end))
print(full_stack)
print("")

front_end.append('Python')
front_end.append('SQL')
full_stack = (' '.join(front_end)) + (' ') + (' '.join(back_end))
print(full_stack)
print("")























