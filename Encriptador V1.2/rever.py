import os
import string

cont1= 0
cont2= 0


def defdesen():
        azlist = 'abcdefghijklmnopqrstuvwxyz'
        print('                                     Seleccione una opción (ingrese 1 o 2):')
        print()
        print()
        print('1. Buscar archivo local (el archivo debe estar en la misma carpeta del programa)')
        print('2. Ingresar string(s) manualmente')
        print()

        seleccion = input('...', )

        if seleccion == '1':

            print('Ingrese el nombre del archivo que desea desencriptar con su extensión...')
            print()
            inputfile = input('File name: ')

            # falta agregar filtro para archivos no existentes
            try:

                po = open(str(inputfile))
                # print(wordList)

            except:

                print('Archivo no encontrado')
                input()
                defdesen()

            #casefold es un lower, pero puede tambien trabajar con UNICODE.
            # print(wordList)
            # somefile= open('Actualizaciones Pendientes.txt')

            po = open(str(inputfile))
            valno = po.read()
            valsi1 = valno.casefold()
            wordList = valsi1.split()
            print(wordList)

        if seleccion == '2':
            # os.system(cls)

            print('Ingrese el string que desea desencriptar: ')
            print()
            valno = input()
            valsi1 = valno.casefold()
            wordList = valsi1.split()
            # wordList.append('done')
            # print(wordList)
            # print(valsi1)

            #wbw= len(wordList)

        else:
            if seleccion != '1':
                print('Opción no valida')
                defdesen()

        final = ''

        contP= 3

            

        for a in wordList:
            fincount= 0 #contador para validar el tamano del string
            pos = 0
            while fincount < (len(a) / 4): # loop que se detiene al llegar al len de la palabra sin encriptar

                 if contP < len(wordList):
                     pos= a[contP]

                     if pos == fincount:
                      contP == contP + 4
                      letra= a[contP - 2] + a[contP - 1]
                      final= final + azlist(letra)
                      fincount= fincount + 1
