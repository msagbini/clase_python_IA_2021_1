# -*- coding: utf-8 -*-
print('Hello world')

# Variables
a = 3
print(type(a))
a = "hola"
print(type(a))

a = 3.5
print(type(a))

a = True
print(type(a))

# suma
a = 5
b = 2
c = a+b
print(c)

# resta

a = 5
b = 2
c = a-b
print(c)

# multiplicacion
a = 5
b = 2
c = a*b
print(c)

# division

a = 5
b = 2
c = a/b
print(c)

a = 5
b = 2
c = a//b
print(c)

# potencia
a = 5
b = 2
c = a**b
print(c)

# raiz cuadrada

a = 16
b = a ** (1/2)
print(b)

# import math
# raiz = math.sqrt(16)

# print(raiz)

# tipos de datos
# string str
a = "Hola Mundo"
a = 'Hola Mundo'
b = "I can't do it"
c = 'Alias Monche'
print(a)
print(b)
print(c)

# entero int
a = 5

# decimal float
a = 5.6

# boolean bool
x = true
y = false

# conversiones entre tipos de datos

# convertir de x a entero

a = '3'
y = float(a)
print(y)
print(type(y))

# convertir de x a  decimal
a = 3
y = float(a)
print(y)
print(type(y))

# convertir de x a string
a = 3
y = str(a)
print(y)
print(type(y))

# concatenaciones

a = 'hola'
b = 'mundo'
c = a + ' ' + b
print(c)

a = 'hola'
b = (a + ' ') * 5
print(b)

# capturar por pantalla

nombre = input('Digite su nombre: ')
print('Hola', nombre)

print('Digite su nombre: ')
nombre = input()
print('Hola', nombre)

# HUA que sume dos números e imprima el resultado
numero_uno = float(input('Digita el número uno: '))
numero_dos = float(input('Digita el número dos: '))
suma = numero_dos + numero_uno
# print(suma)
# print('La suma es: ', suma)
print(f'La suma es: {suma}')

# HUA que lea un número y lo eleve al cuadrado


numero = float(input('Digite el número que desea elevar al cuadrado: '))
cuadrado = numero**2
print(f' El número {numero} elevado al cuadrado es: {cuadrado}')

# HUA que tome el valor de un producto, le aplique el 20% desc
# imprime valor inicial
# valor con descuento, valor ahorrado

valor_producto = float(input('Digite el valor del producto: '))
valor_descuento = valor_producto * 0.8
valor_ahorrado = valor_producto * 0.2
print(f'El valor del producto inicial es de: {valor_producto}')
print(f'El valor ahorrado fue: {valor_ahorrado}')
print(f'El valor del producto con descuento: {valor_descuento}')

# condicionales

# tabla de verdad

# tabla del and
# v and v = v
# v and f = f
# f and f = f
# f and v = f

# tabla del or
# v or v = v
# v or f = v
# f or f = f
# f or v = v

# tabla del and
print(True and True)
print(True and False)
print(False and False)
print(False and True)


# tabla del or

print(True or True)
print(True or False)
print(False or False)
print(False or True)

# Negacion

print(not True)
print(not False)

# Jerarquía de operaciones
# 1. Paréntesis y llaves
# 2. Potencias y raices
# 3. Multiplicación y división
# 4. Suma y resta

# Jerarquía de operaciones booleanas
# 1. Paréntesis y llaves
# 2. Tabla de verdad (de izq a derecha)

# Más de 2 condiciones al mismo tiempo
print(True and False and True or False or True or True)
print(True and (False and True) or False or (True or True))

# Estructura if

if (x > 0):
    print('1')
else:
    print('2')
print('3')


# HUA que dada la edad de una persona, indique si es mayor o menor de edad

edad = int(input("Digite la edad: "))
if (edad >= 18):
    print('Es mayor de edad')
else:
    print('Es menor de edad')

# HUA que indique si el estudiante aprobó o reprobó
nota = float(input("Digite la nota: "))
if nota < 0 or nota > 5:
    print('No es una nota válida')
elif (nota >= 3):
    print('Aprobó')
else:
    print('Reprobó')


# HUA que dado un número n diga si es negativo, positivo o cero

numero = float(input("Digite el número: "))

if numero > 0:
    print('El número es positivo')
elif (numero < 0):
    print('El número es negativo')
else:
    print('El número es 0')





























































































