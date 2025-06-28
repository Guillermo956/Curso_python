'''
crear un programa que pidad dos numeros 
y que obtenga como resultados cual de ellos es par 
o si ambos lo son.
#si ambos son pares, mostrar el mensaje "ambos son pares"
#si uno es par y otro impar, mostrar el mensaje "uno es par y otro impar
'''
n1 = int(input("Ingrese el primer numero: "))    
n2 = int(input("Ingrese el segundo numero: "))
if n1 % 2 == 0 and n2 % 2 == 0:
    print("Ambos son pares")
elif n1 % 2 == 0 and n2 % 2 != 0:
    print("Uno es par y otro impar")

