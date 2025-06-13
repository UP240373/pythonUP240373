


#       Ejercicios 1 a 3

edad = int(18)
peso = float(90)
imagine = complex(1 + 5j)

print("")
print("")
print("")



#       Ejercicios 4

area = 0.5 * int(input('Ingresa la base del trinagulo: ')) * int(input('Ingresa la altura del triangulo: '))
print('El area del triangulo es de: ', area)

print("")
print("")
print("")



#       Ejercicios 5

perimetro = int(input('lado a: ')) + int(input('lado b: ')) + int(input('lado c: '))
print('El perimetro del triangulo es de: ', perimetro)

print("")
print("")
print("")



#       Ejercicios 6

ancho = int(input('Introduce el ancho del rectangulo: ')) 
alto = int(input('Introduce el alto del rectangulo: '))
print("")

print('El area del rectangulo es: ', ancho * alto)
print('El perimetro del rectangulo es: ', 2 * (ancho + alto))

print("")
print("")
print("")



#       Ejercicios 7

pi = 3.14
radio = int(input('Introduce el radio del circulo: ')) 
print("")

print('El area del circulo es: ', pi * (radio**2))
print('El perimetro del circulo es: ', 2 * pi * radio)

print("")
print("")
print("")



#       Ejercicios 8

xintercept = int(input('"y = 2x-2"  Introduce el valor de x: ')) 
xintercept = (2 * xintercept) - 2
print("")

print('y = ', xintercept)

print("")
print("")
print("")



#       Ejercicios 9

x1 = 2 
x2 = 6 
y1 = 2 
y2 = 10

print('La formula es: m = y2-y1/x2-x1') 
m = (y2 - y1) / (x2 - x1)
print("")

print('m = (10) - (2) / (6) - (2)', m)

print("")
print("")
print("")



#       Ejercicios 10

print('El valor del inciso 8 es; ', xintercept) 
print('El valor del inciso 9 es; ', m) 
print("")

print('El valor mas grande es: ', max(xintercept, m))

print("")
print("")
print("")



#       Ejercicios 11

y = float(input('Introduce el valor de y para "y = x^2 + 6x + 9": ',)) 
print("")

print('El valor de y es: ', (y ** 2) + (6 * y) +9)

print("")
print("")
print("")



#       Ejercicios 12

text1 = 'python'
text2 = 'dragon'
print("")

print('La longitud de', text1, 'es de: ', len(text1))
print('La longitud de', text2, 'es de: ', len(text2))
print('la variable mas larga tiene: ', max(len(text1), len(text2)), ' caracteres')

print("")
print("")
print("")



#       Ejercicios 13

print('¿"on" esta dentro de:', text1, 'y', text2, '? = ', ('on' in text1) and ('on' in text2))

print("")
print("")
print("")



#       Ejercicios 14

print('¿jargon in "I hope this course is not full of jargon" ? = ','jargon' in 'I hope this course is not full of jargon')

print("")
print("")
print("")



#       Ejercicios 15

print('¿"on" no esta dentro de:', text1, 'y', text2, '? = ',('on' not in text1) and ('on' not in text2))

print("")
print("")
print("")



#       Ejercicios 16

print(text1)
convert = len(text1)
print(convert)
convert = float(convert)
print(convert)
convert = str(convert)
print(convert)

print("")
print("")
print("")



#       Ejercicios 17

n = int(input('Introduce un numero: '))
print('¿', n, 'es un numero par?', (n % 2) == 0)


print("")
print("")
print("")



#       Ejercicios 18

n1 = float(7)
n2 = float(2.7)

print('¿(', n1, '/ 3 ) es igual a (', n2, ')? =', (n1 / 3) == (int(n2)))


print("")
print("")
print("")



#       Ejercicios 19

print('¿"10" es igual a 10? =','10' == 10)


print("")
print("")
print("")



#       Ejercicios 20

n1 = int(9.8)
n2 = int(10)
print('¿"int(9.8)" es igual a 10? =',n1 == n2)


print("")
print("")
print("")



#       Ejercicios 21

n1 = int(input('Introduce las horas = '))
n2 = int(input('Introduce la tarifa por hora = '))
print("")

print('Su ganancia semanal es de: ',n1 * n2)

print("")
print("")
print("")



#       Ejercicios 22

n1 = int(input('Introduce el numero de años que has vivido = '))
print('Has vivido por',n1 * 365 * 24 * 3600, 'segundos')

print("")
print("")
print("")



#       Ejercicios 23

n1 = 1
print(n1, n1, n1, n1, n1)
print(n1 + 1, n1, n1 + 1, n1 + 3, n1 + 7)
print(n1 + 2, n1, n1 + 2, n1 + 8, n1 + 26)
print(n1 + 3, n1, n1 + 3, n1 + 15, n1 + 63)
print(n1 + 4, n1, n1 + 4, n1 + 24, n1 + 124)

print("")
print("")
print("")


