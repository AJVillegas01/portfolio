import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
#model[A,B,C,D]
#array[CDBA]
print('Introduce model')
model = input()
print('Introduce sequence')
array = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print('Los valores del array que no coinciden y sus posiciones en esta misma son los siguientes:')
for i in range(len(array)):
    if array[i] != model[i]:
        difference = array[i]
        position = i
        print(difference, i)
for indice_a, elemento_a in enumerate(model):
    for indice_b, elemento_b in enumerate(array):
        if elemento_a == elemento_b:
            print(f"El valor {elemento_a} del modelo en la posición {indice_a} coincide con el array en la posicion {indice_b} del array")
