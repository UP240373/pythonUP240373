
print('\n\n')

#       Ejercicios 1

n = 0

for i in range(101):
    n += i
print('The sum of all numbers is', n)

print('\n\n')


#       Ejercicios 2

evens, odds = 0, 0

for i in range(101):
    if i % 2 == 0:
        evens += i
    if i % 2 != 0:
        odds += i
print(f'The sum of all evens is {evens}. And the sum of all odds is {odds}')

print('\n\n')