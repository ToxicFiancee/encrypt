import os
import string

letra= ""
contP= 0
print('Ingrese el nombre del archivo que desea encriptar con su extensión...')
print()
inputfile= input('File name: ')
po= open(str(inputfile))
#somefile= open('Actualizaciones Pendientes.txt')
valno= po.read()
valsi1= valno.casefold()
wordList= valsi1.split()
print(wordList)
input()
file =open("salida2.txt", "w")

for a in wordList:
    contP= 3
    contI= str(contP)
    file.write(a)
    print(a)
    letra= a[contP - 2] + a[contP - 1]
    #letra= str(a(ContP)) + str(a(ContP - 1))
    print(letra)
    input()

file.close()





input('break a contiuacion')


#Manipulating Lists
