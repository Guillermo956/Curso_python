'''
condiciones if, elif, else
'''
datos=int(input('Ingrese un numero: '))
if datos > 0:
    print('El numero es positivo')
elif datos < 0:
    print('El numero es negativo')
else:
    print('El numero es cero')

#un if
if datos % 2 == 0:
    print('El numero es par')

#if else
if datos % 2 == 0:
    print('El numero es par')
else:   
    print('El numero es impar')

# if elif else
if datos % 2 == 0:  
    print('El numero es par')   
elif datos % 2 == 1:
    print('El numero es impar')
elif datos == 0:
    print('El numero es cero') 
else:
    print('El numero es cero')  