
print('\n\n')

#       Ejercicios 1

n = 0

while n <= 10:
    print(n)
    n += 1

print('\n\n')


#       Ejercicios 2

n = 10

while n >= 0:
    print(n)
    n -= 1

print('\n\n')


#       Ejercicios 3

n = 1

while n <= 7:
    print(n * '#')
    n += 1

print('\n\n')


#       Ejercicios 4

n = 8

for i in range(n):
    for j in range(n):
        print('# ', end="")
    print()

print('\n\n')


#       Ejercicios 5

n, a, b = 0, 0, 0

while n <= 10:
    a, b = n, n
    print(f'{a} x {b} = {a * b}')
    n += 1

print('\n\n')


#       Ejercicios 6

lt = ['Python', 'Numpy','Pandas','Django', 'Flask']

for i in lt:
    print(i)

print('\n\n')


#       Ejercicios 7

for i in range(102):
    if i % 2 == 0:
        print(i)

print()


#       Ejercicios 8

for i in range(100):
    if i % 2 != 0:
        print(i)

print()







