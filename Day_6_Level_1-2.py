
print('\n\n')

""" Nivel 1 """

#       Ejercicios 1

tp1 = ()
print(tp1)

print('\n\n')


#       Ejercicios 2

sisters = ('Gaby', 'Araceli')
brothers = ('Angel', 'Juan')
print('Hermanas =', sisters)
print('Hermanos =', brothers)

print()


#       Ejercicios 3

siblings = sisters + brothers
print('Hermanos y Hermanas =', siblings)

print()


#       Ejercicios 4

print('Tengo:', len(siblings), 'hermanos')

print()


#       Ejercicios 5

family_members = siblings + ('Jose', 'Norma')
print('Miembros de la familia:', family_members)

print('\n\n')




""" Nivel 2 """

#       Ejercicios 1

del family_members


#       Ejercicios 2

fruits = ('Manzana', 'Naranja', 'Piña', 'Pepino')
vegetables = ('Tomate', 'Zanahoria', 'Cebolla', 'Chayote')
animal_products = ('Queso', 'Tocino', 'Chorizo', 'Huevo')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

print()


#       Ejercicios 3

food_stuff_lt = list(food_stuff_tp)
print(type(food_stuff_lt))

print()


#       Ejercicios 4

half = (len(food_stuff_tp) / 2)
mitad_de_food = food_stuff_tp[0:int(half)]
print(mitad_de_food)

print('\n\n')


#       Ejercicios 5

primeros_3_items = food_stuff_lt[0:3]
ultimos = len(food_stuff_lt) - 3
ultimos_3_items = food_stuff_lt[ultimos::]
print(primeros_3_items)
print(ultimos_3_items)

print('\n\n')


#       Ejercicios 6

del food_stuff_tp


#       Ejercicios 7

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)

print()

