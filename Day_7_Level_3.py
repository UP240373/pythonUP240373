
print('\n\n')

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = {22, 19, 24, 25, 26, 24, 25, 24}


#       Ejercicios 1

lst = list(age)
print(age == lst)

print()


#       Ejercicios 2

str = str(age)
print(type(str), str)
print(type(lst), lst)
tpl = tuple(age)
print(type(tpl), tpl)
print(type(age), age)

print()


#       Ejercicios 3

txt = 'I am a teacher and I love to inspire and teach people'
lst = " ".join(txt)
st1 = set(lst)
print(st1)

print()



