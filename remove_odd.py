#Elimina los numeros impares del lista original usando como apoyo la lista auxiliar en menos de un segundo
#El metodo .remove() tiene complejidad algoritmica lineal y nos crea una nueva lista con los elementos restantes cada vez que elimnamos un elemento
import time

lista_original = list(range(1,101))
print(lista_original)
lista_auxiliar = range(1,101,2) #se puede optimizar incluso mas si ponemos set(), es decir: set(range(1,101,2))
print(lista_auxiliar)

inicio = time.time()
##########################################
"""for element in lista_auxiliar:
    lista_original.remove(element)
print(lista_original)""" # esto tarda mucho

#utilizamos list comprenhension
lista_nueva = [element for element in lista_original
               if element not in lista_auxiliar]
print(lista_nueva)


######################################
fin = time.time()
print(fin-inicio)