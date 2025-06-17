import random
import string
import os


def encriptar():
    os.system('cls')
    azlist = 'abcdefghijklmnopqrstuvwxyz'
    print('                                     Seleccione una opción (ingrese 1 o 2):')
    print()
    print()
    print('1. Buscar archivo local (el archivo debe estar en la misma carpeta del encriptador)')
    print('2. Ingresar string(s) manualmente')
    print()

    seleccion = input('...', )

    if seleccion == '1':

        print('Ingrese el nombre del archivo que desea encriptar con su extensión...')
        print()
        inputfile = input('File name: ')

        # falta agregar filtro para archivos no existentes
        try:

            po = open(str(inputfile))
            # print(wordList)

        except:

            print('Archivo no encontrado')
            input()
            encriptar()

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

        print('Ingrese el string que desea encriptar: ')
        print()
        valno = input()
        valsi1 = valno.casefold()
        wordList = valsi1.split()
        # wordList.append('done')
        # print(wordList)
        # print(valsi1)

        # wbw= len(wordList)

    else:
        if seleccion != '1':
            print('Opción no valida')
            encriptar()

    final = ''

    for a in wordList:  # Filtro para varios strings separados con espacios

        valsi2 = a

        if final != '':
            final = final + ' '

        for i in azlist:  # Aqui recorre el abecedario para validar cada letra
            cont = -1
            cont2 = 0

            # print(final)

            for n in valsi2:  # Aqui recorre el string buscando especificamente la letra correspondiente
                cont = cont + 1
                if n == i:
                    cont2 = cont2 + 1
                    if cont2 == 1:
                        x = random.choice(azlist)
                        final = final + x  # agrega una letra al azar
                        validacion = azlist.find(i) - 10  # agregar cero si la letra del abecedario es menor a 10
                        if validacion < 0:  # agregar cero si la letra del abecedario es menor a 10
                            final = final + '0'

                        final = final + str(azlist.index(i))

                    final = final + str(cont)

                # pos= len(final) #bloque para agregar el numero correspondiente a la letra del abecedario luego de la letra azar
                # pos= pos - 1
                # pos2= final[pos]

                # print(pos2)

                # if pos2.isdigit():
                #    print()
                # else:
                #    if n == i:

    # Falta:
    # 1 Agregar filtro para palabras con mas de 10 caracteres, de manera que el programa lo divida
    # en dos strings. Para que pueda unirlos otra vez al ser desencriptados, estos string tendran una letra
    # adicional al inicio y al final (para el primer string al final, y para el segundo al principio). Asi se
    # indentificara donde inicia la palabra y donde termina para que puedan ser unidas.
    # 2 Agregar filtro para espacios (IMPLEMENTADO)
    # 3 Agregar filtro para caractares especiales
    # Se implento seleccion de archivo o ingreso de strig manual, asi como la creacio de archivo con texto encriptado

    print(final)
    file = open("salida.txt", "w")
    file.write(final)
    file.close()

    input()
