
print('\n\n')

#       Ejercicios 1

calificacion = 0 #int(input('Introduce tu calificacion: '))

if calificacion <= 100 and calificacion >= 90:
    print('Sacaste una A')
elif calificacion < 90 and calificacion >= 70:
    print('Sacaste una B')
elif calificacion < 70 and calificacion >= 60:
    print('Sacaste una C')
elif calificacion < 60 and calificacion >= 50:
    print('Sacaste una D')
elif calificacion < 50 and calificacion >= 0:
    print('Sacaste una F')

print()

#       Ejercicios 2

mes = 0 #str(input('Introduce un mes: '))

if mes == 'septiembre' or mes == 'octubre' or mes == 'noviembre':
    print('Es temporada de otoño')
elif mes == 'diciembre' or mes == 'enero' or mes == 'febrero':
    print('Es temporada de invierno')
elif mes == 'marzo' or mes == 'abril' or mes == 'mayo':
    print('Es temporada de primavera')
elif mes == 'junio' or mes == 'julio' or mes == 'agosto':
    print('Es temporada de verano')
else: 
    print('No se reconocio el mes, revisa haberlo escrito correctamente')

print()


#       Ejercicios 3

fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = str(input('Introduce una fruta: '))

if (new_fruit in fruits) == False:
    fruits[(len(fruits) - 1)] = new_fruit
    print(fruits)
else:
    print('That fruit already exist in the list')

print()




