
print('\n\n')

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


#       Ejercicios 1

print(len(it_companies))

print()


#       Ejercicios 2

it_companies.add('Twitter')
print(it_companies)

print()


#       Ejercicios 3

it_companies.update(['Samsung','Xiaomi','Intel','Cisco'])
print(it_companies)

print()


#       Ejercicios 4

it_companies.remove('Cisco')
print(it_companies)

print()


#       Ejercicios 5

it_companies.pop()
print('Descartar = Remover un item random:', it_companies)




