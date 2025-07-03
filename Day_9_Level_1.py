
print('\n\n')

#       Ejercicios 1

edad = int(input('Enter your age: '))

if edad >= 18:
    print('You are old enough to learn to drive.')
else: 
    need = 18 - edad
    print(f'You need {need} more years to learn to drive.')

print()

#       Ejercicios 2

my_age = 18
your_age = int(input('Enter your age: '))

if my_age > your_age:
    difference = my_age - your_age
    if difference == 1:
        print(f'I am {difference} year older than you')
    else:
        print(f'I am {difference} years older than you')
elif your_age > my_age:
    difference = your_age - my_age
    if difference == 1:
        print(f'You are {difference} year older than me')
    else:
        print(f'You are {difference} years older than me')
else:
    print('We have the same age')

print()


#       Ejercicios 3

a = int(input('Enter number one: '))
b = int(input('Enter number two: '))

if a > b:
    print(f'{a} is greater than {b}')
elif b > a:
    print(f'{b} is greater than {a}')
else:
    print(f'{a} is equal to {b}')




