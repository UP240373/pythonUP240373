
print('\n\n')

# Directorio personal 

person={
    'first_name': 'Abdul',
    'last_name': 'Martinez Campos',
    'age': 18,
    'country': 'Mexico',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Lopez Mateos',
        'zipcode': '5020'
    }
    }

#       Ejercicios 1

if 'skills' in person:
    middle = int((len(person['skills'])) / 2)
    print(person['skills'][middle])

print()

#       Ejercicios 2

if 'skills' in person:
    if 'Python' in person['skills']:
        print('Existe Python en skills')
    else:
        print('No existe Python en skills')

print()


#       Ejercicios 3

if ('React' in person['skills']) and ('Node' in person['skills']) and ('MongoDB' in person['skills']):
    print('He is a fullstack developer')
elif ('JavaScript' in person['skills']) and ('React' in person['skills']):
    print('He is a front end developer')
elif ('Node' in person['skills']) and ('Python' in person['skills']) and ('MongoDB' in person['skills']): 
    print('He is a backend developer')
else:
    print('unknown title')

print()


#       Ejercicios 4

if (person['is_married'] == True) and (person['country'] == 'Mexico'):
    print(f'{person["first_name"]} {person["last_name"]} lives in Mexico. He is married.')

print()




