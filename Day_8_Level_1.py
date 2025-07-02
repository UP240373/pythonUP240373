
print('\n\n')

#       Ejercicios 1

dog = {}


#       Ejercicios 2

dog = {
    'name':'Canela', 
    'breed': 'White and Brown',
    'legs': 4,
    'age': 15
}
print(dog)

print('\n\n')


#       Ejercicios 3

student_1 = {
    'first_name': 'Angel', 
    'last_name': 'Campos', 
    'gender': 'Male', 
    'age': 18, 
    'marital status': False, 
    'skills': ['C++', 'Python', 'JavaScript'], 
    'country': 'Mexico', 
    'city': 'Aguascalientes', 
    'address': 'Lopez Mateos'
}
print('Estudiante 1:', student_1)

print()


#       Ejercicios 4

print(len(student_1))

print()


#       Ejercicios 5

skills_1 = student_1['skills']
print(skills_1, type(skills_1))

print()


#       Ejercicios 6

student_1['skills'].append('C#')
student_1['skills'].append('html')
print(student_1['skills'])

print('\n\n')


#       Ejercicios 7

keys = student_1.keys()
print(keys)

print()


#       Ejercicios 8

values = student_1.values()
print(values)

print()


#       Ejercicios 9

print(student_1.items())

print()


#       Ejercicios 10

student_1.popitem()
print(student_1)

print()


#       Ejercicios 11

del student_1














