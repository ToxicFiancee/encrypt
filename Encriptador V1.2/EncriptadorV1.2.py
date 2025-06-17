# Encriptador
import os

from defEncrip import encriptar
from rever import defdesen


azlist = 'abcdefghijklmnopqrstuvwxyz'

def Inicio():
    print("Entre a inicio")
    valne= input('Ingrese el texto que desea encriptar: ')
    print('A continuación se procederá a encriptar el string ingresado ')

    return valne

sel= ''
while sel != 4:   #Menu
    os.system('cls')
    print('Bienvenido al Encriptador')
    print()
    print()
    print('Escriptador creado por ToxicFiancee')
    print('v1.2')
    print()
    print()
    print('Menu')
    print('(Ingrese el número correspondiente a la acción que desea realizar)')
    print()
    print('1. Encriptar')
    print('2. Desencriptar (Solo para strings encriptados con la versión 1.2)')
    print('3. FAQ')
    print('4. Salir')
    sel= input()
    if '1' == sel:
        encriptar()
        continue
    if '2' == sel:
        defdesen()
        
        continue
    if '3' == sel:
        print('En desarrollo')
        continue
    if '4' == sel:
        break
#    elif
    print ('Opción no válida')
    input()
    

sel.rstrip()
