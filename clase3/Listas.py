'''
EJemplo de listas en Python
'''
array = ["futbol","pc",18.6,18,[6,7,10.4],True,False]
print(array)
#acceso a un elemento de la lista
print(array[0])  
print(array[4])
print(array[4][2])  # Acceso al tercer elemento de la sublista
print(array[0:3])  # Acceso a los primeros tres elementos
print(len(array))  # Longitud de la lista
array.append(66)  # Añadir un elemento al final de la lista
print(array)
array.insert(2, "nuevo")  # Insertar un elemento en la posición 2
print(array)
array.extend(["nuevo1", "nuevo2"])  # Añadir varios elementos al final
print(array)
array.remove("futbol")  # Eliminar un elemento específico
print(array)
array.pop()  # Eliminar el último elemento
print(array)
array.pop(2)  # Eliminar el elemento en la posición 2
print(array)
array.clear()  # Limpiar la lista
print(array)  # Imprimir la lista vacía
array = ["futbol", "pc", 18.6, 18, [6, 7, 10.4], True, False]
array2 = ["baki", "goku", "vegeta"]
array3 = array + array2  # Concatenar dos listas
print(array3)  # Imprimir la lista concatenada
print("futbol" in array)  # Comprobar si un elemento está en la lista
print(array.index("pc"))  # Obtener el índice de un elemento
print(array.count(18))  # Contar cuántas veces aparece un elemento
array4 = [1,2,3,4,5,6,7,8,9,10]
array4.reverse()  # Invertir el orden de la lista
print(array4)  # Imprimir la lista invertida
array5 = [4,6,1,2,3,5,7,8,9,10]
array5.sort()  # Ordenar la lista
print(array5)  # Imprimir la lista ordenada