
#       Ejercicios 1 

text1 = 'Thirty'
text2 = 'Days' 
text3 = 'Of'
text4 = 'Python' 
space = ' '

text_complete = text1 + space + text2 + space + text3 + space + text4
print(text1)
print(text2)
print(text3)
print(text4)
print(text_complete)

print('\n\n')


#       Ejercicios 3

company = 'Coding For All'


#       Ejercicios 4

print(company)


#       Ejercicios 5 

print(len(company))

print('\n\n')


#       Ejercicios 6 

print(company.upper())


#       Ejercicios 7 

print(company.lower())

print('\n\n')


#       Ejercicios 8 

print(company.title())


#       Ejercicios 9 

print(company.strip('Coding'))


#       Ejercicios 10 

print(company.startswith('Coding'))


#       Ejercicios 11

company = company.replace('Coding', 'Python')
print(company)


#       Ejercicios 12

print(company.replace('Python', 'Everyone to Python'))
print("")


#       Ejercicios 13

print(company.split())
print("")

#       Ejercicios 14

Apps = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(Apps.split(', '))
print("")


#       Ejercicios 15

company = 'Coding For All'
print('Caracter num 0:', company[0])
print("")


#       Ejercicios 16

print('Ultimo caracter:', company[-1])
print("")


#       Ejercicios 17

print('Caracter num 10:',company[10])

print("")
print("")
print("")


#       Ejercicios 18

company = 'Python For Everyone'
text1 = company[0:2] + company[7:10] + company[11:14]
print('Acronimo de \"Python For Everyone\": ', text1)
print("")


#       Ejercicios 19

company = 'Coding For All'
text1 = company[0:3] + company[7] + company[11:14]
print('Acronimo de \"Coding For All\": ', text1)

print('\n\n')


#       Ejercicios 20

company = 'Coding For All'
text1 = 'C'

print(company.index(text1))  
print("")


#       Ejercicios 21

text1 = 'F'

print(company.index(text1))  
print("")


#       Ejercicios 22

company = 'Coding For All People'
text1 = 'l'

print(company.rfind(text1))  

print('\n\n')


#       Ejercicios 23

company = 'You cannot end a sentence with because because because is a conjunction'
text1 = 'because'

print('Primera posicion del string con la palabra \"because\": ', company.find(text1))  
print("")


#       Ejercicios 24

company = 'You cannot end a sentence with because because because is a conjunction'
text1 = 'because'

print('Ultima posicion del string con la palabra \"because\": ', company.rfind(text1))  














