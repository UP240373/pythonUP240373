
print('\n\n')

#       Ejercicios 1

n = 100 #int(input('Introduce un numero: '))

def evens_and_odds(n):
    cont_odds = 0
    cont_evens = 0

    for i in range(0, n + 1):
        if i % 2 == 0:
            cont_evens += 1
        else:
            cont_odds += 1
    
    print('The number of odds are', cont_odds)
    print('The number of evens are', cont_evens)

evens_and_odds(n)

print('\n\n')


#       Ejercicios 2

n = 5 #int(input('Introduce un numero: '))

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(n))

print('\n\n')


#       Ejercicios 3

lst1 = []
lst2 = [1, 2, 3, 4, 5]

def is_empty(text):
    if len(text) == 0:
        return 'la variable esta vacia'
    else:
        return 'la variable no esta vacia'

print(is_empty(lst1))
print(is_empty(lst2))

print('\n\n')

#       Ejercicios 4

lst = [37, 89, 45, 61, 22, 13, 98, 73, 55, 6, 80, 34, 59, 11, 47, 76, 90, 28, 7, 68, 84, 66, 20, 35, 92, 39, 99, 52, 8, 70]

def calculate_mean(lst):
    suma_total = 0
    for i in lst:
        suma_total += i
    media = (suma_total) / (len(lst))
    return round(media, 3)

def calculate_median(lst):
    lst = list(lst)
    mediana = 0
    i = 0
    valor_2 = lst[0]
    while i < len(lst):
        valor_1 = lst[i]
        if valor_1 < valor_2:
            lst.pop(i)
            lst.insert(0, valor_1)
            i = 0
            valor_2 = lst[0]
        else: 
            valor_2 = valor_1
        i += 1
    middle = int((len(lst)) / 2)
    if len(lst) % 2 == 0:
        parte_1 = lst[0:middle]
        parte_2 = lst[middle::]
        mediana = parte_1[-1] + parte_2[0]
    else:
        mediana = lst[middle]
    mediana /= 2
    return mediana

def calculate_mode(lst):
    frecuencias = {}
    for elemento in lst:
        frecuencias[elemento] = frecuencias.get(elemento, 0) + 1

    moda = None
    max_frecuencia = 0
    for elemento, frecuencia in frecuencias.items():
        if frecuencia > max_frecuencia:
            moda = elemento
            max_frecuencia = frecuencia
    return moda

def calculate_range(lst):
    rango = max(lst) - min(lst)
    return rango

def calculate_variance(lst):
    sum = 0
    media = calculate_mean(lst)
    for i in lst:
        sum += (i - media) ** 2
    varianza = sum / ((len(lst)) - 1)
    return varianza

def calculate_std(lst):
    std = calculate_variance(lst) ** 0.5
    return round(std, 3)


def probability_functions(lst):
    print(lst, '\n')
    print('La media es:', calculate_mean(lst))
    print('La mediana es:', calculate_median(lst))
    print('La moda es:', calculate_mode(lst))
    print('El rango es:', calculate_range(lst))
    print('La varianza es:', calculate_variance(lst))
    print('La desviacion estandar es:', calculate_std(lst))

probability_functions(lst)

print('\n\n')