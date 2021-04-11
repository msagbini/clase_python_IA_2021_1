"""

@author: RYZEN
"""

from statistics import mode


def es_primo(posicion):
    for n in range(2, posicion):
        if posicion % n == 0:
            print('No es un número primo')
            return False
        print('Es un número primo')
        vector_primo.append(posicion)
        return True


# Punto1

vector1 = []
productoria = 1
vector_productoria = []
sumatoria = 0
vector_sumatoria = []


tamaño1 = int(input('Digite la cantidad de elementos del vector: '))
for i in range(tamaño1):
    posicion = float(input(f'Digite el numero en la posicion {i} del vector:  '))
    sumatoria = sumatoria + posicion
    productoria = productoria * posicion
    vector1.append(posicion)
    vector_sumatoria.append(sumatoria)
    vector_productoria.append(productoria)
print(f'Los elementos del vector son: {vector1}')
print(f'La sumatoria es: {sumatoria} ')
print(f'La productoria es: {productoria} ')
print(f'El elemento de mayor valor del vector es: {max(vector1)}')
print(f'El elemento de menor valor del vector es: {min(vector1)}')

# Punto2

vector2 = []
vector_par = []
vector_impar = []
vector_primo = []
tamaño2 = int(input('Digite la cantidad de elementos del vector: '))
for i in range(tamaño2):
    posicion2 = int(input(f'Digite el numero en la posicion {i} del vector: '))
    vector2.append(posicion2)
    if(posicion2 % 2 == 0):
        es_primo(posicion2)
        vector_par.append(posicion2)
    else:
        es_primo(posicion2)
        vector_impar.append(posicion2)
print(f'Los elementos del vector son : {vector2}')
print(f'Los numeros pares son : {vector_par}')
print(f'Los numeros impares son : {vector_impar}')
print(f'Los numeros primos son : {vector_primo}')

# Punto3

vector3 = []
vector4 = []
vector_suma = []
vector_resta = []
tamaño3 = int(input('Digite la cantidad de elementos de los vectores: '))
for i in range(tamaño3):
    posicion3 = float(input(f'Digite el número en la posicion {i}: '))
    posicion4 = float(input(f'Digite el número en la posicion {i}: '))
    suma = posicion3 + posicion4
    resta = posicion3 - posicion4
    vector3.append(posicion3)
    vector4.append(posicion4)
    vector_resta.append(resta)
    vector_suma.append(suma)
print(f'Los elementos del vector 1 son: {vector3}')
print(f'Los elementos del vector 2 son: {vector4}')
print(f'El resultado de su suma es: {vector_suma}')
print(f'El resultado de su resta es: {vector_resta}')

# Punto4

vector5 = []
tamaño4 = int(input('Digite la cantidad de elementos del vector: '))
for i in range(tamaño4):
    posicion5 = float(input(f'Digite el número en la posición {i}: '))
    vector5.append(posicion5)
print(f'El numero que más se repite es: {mode(vector5)}')

# Punto5

vector6 = []
vector_productoria2 = []
vector_sumatoria2 = []
vectorq = []
productoria2 = 1
sumatoria2 = 0
tamaño5 = int(input('Digite la cantidad de elementos del vector: '))
par = int(tamaño5 / 2)
if(tamaño5 % 2 == 0):
    for i in range(par):
        posicion6 = float(input(f'Digite el numero de la primera mitad del vector en la posicion {i}: '))
        productoria2 = productoria2 * posicion6
        vector_productoria2.append(productoria2)
        vector6.append(posicion6)
        vectorq.append(productoria2)
    for i in range(par):
        posicion7 = float(input(f'Digite el numero de la segunda mitad del vector en la posicion {i}: '))
        sumatoria2 = sumatoria2 + posicion7
        vector_sumatoria2.append(sumatoria2)
        vector6.append(posicion7)
        vectorq.append(sumatoria2)
    print(f'El vector es: {vector6}')
    print(f'Su productoria es: {productoria} y su vector en la primera mitad es : {vector_productoria2}')
    print(f'Su sumatoria es: {sumatoria2} y su vector en la segunda mitad es: {vector_sumatoria2}')
    print(f'El vector resultante es : {vectorq}')
else:
    print('Por favor digite una longitud par')
    
vector6 = []
vector_productoria = []
vector_sumatoria = []
vector = []
productoria = 1
sumatoria = 0
tamaño5 = int(input('Digite la cantidad de elementos del vector: '))
par = int(tamaño5 / 2)
if(tamaño5 % 2 == 0):
    for i in range(par):
        posicion6 = float(input(f'Digite el número de la 1ra mitad en {i}: '))
        productoria = productoria * posicion6
        vector_productoria.append(productoria)
        productoria.append(posicion6)
        vector.append(productoria)
    for i in range(par):
        posicion7 = float(input(f'Digite el numero de la 2daa mitad en {i}: '))
        sumatoria = sumatoria + posicion7
        vector_sumatoria.append(sumatoria)
        productoria.append(posicion7)
        vector.append(sumatoria)
    print(f'El vector es: {productoria}')
    print(f'Su productoria es: {productoria} y su vector en la primera mitad es: {vector_productoria}')
    print(f'Su sumatoria es: {sumatoria} y su vector en la segunda mitad es: {vector_sumatoria}')
    print(f'El vector resultante es : {vector}')
else:
    print('Por favor digite una longitud de vector que sea par')


# Punto6

vector7 = []
tamaño = int(input('Digite la cantidad de elementos del vector: '))
if(tamaño % 2 == 0):
    for i in range(tamaño):
        posicion = float(input(f'Digite el número del vector en la posicion {i}: '))
        vector7.append(posicion)
    medio = int(len(vector7) / 2)
    primeramitad = vector7[:medio]
    segundamitad = vector7[medio:]
    if(primeramitad == segundamitad[::-1]):
        print(f'El vector {vector7} es simétrico')
    else:
        print(f'El vector {vector7} no es simétrico')
elif(tamaño <= 1):
    print('Digite un número mayor a 1')
else:
    for i in range(tamaño):
        posicion2 = float(input(f'Digite el número del vector en la posición {i}: '))
        vector7.append(posicion2)
    print(f'El vector es : {vector7}')
    medio = int(len(vector7) / 2)
    vector7.pop(medio)
    primeramitad = vector7[:medio]
    segundamitad = vector7[medio:]
    if(primeramitad == segundamitad[::-1]):
        print(f'El vector sin el número de de la mitad es: {vector7} y es simetrico')
    else:
        print('El vector no es simetrico')

# Punto7

vectora = []
vectorb = []
tamaño = int(input('Digite la cantidad de elementos para cada vector: '))
for i in range(tamaño):
    posiciona = float(input(f'Digite el numero del vector A en la posicion: {i} '))
    vectora.append(posiciona)
for i in range(tamaño):
    posicionb = float(input(f'Digite el número del vector B en la posicion {i}: '))
    vectorb.append(posicionb)
va = set(vectora)
vb = set(vectorb)
union = va | vb
interseccion = va & vb
diferenciaAB = va - vb
diferenciaBA = va - vb
print(f'La union tiene como elementos : {union} ')
print(f'La interseccion tiene como elementos : {interseccion} ')
print(f'La diferencia de A - B tiene como elementos : {diferenciaAB} ')
print(f'La diferencia de B - A tiene como elementos : {diferenciaBA} ')
