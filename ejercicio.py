# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 20:41:53 2021

@author: RYZEN
"""
# Ejercicio 1
cantidad_camisas = float(input('Digite cuántas camisas va adquirir: '))
valor_compra = cantidad_camisas * 50000
if cantidad_camisas <= 0:
    print('No es un valor válido')
elif cantidad_camisas >= 3:
    valor_compra = valor_compra*0.7
    print(f'El valor a pagar con el 30% de descuento es de: {valor_compra}')
else:
    valor_compra = valor_compra*0.9
    print(f'El valor a pagar con el 10% de descuento es de: {valor_compra}')

# Ejercicio 2

valor_compra = float(input('Digite el valor de su compra: '))
valor_numero = float(input('Escoja un número: '))

if valor_numero < 74:
    valor_compra = valor_compra*0.15
    print(f'Descuento Aplicado del 15% por un valor de {valor_compra}')
else:
    valor_compra = valor_compra*0.20
    print(f'Descuento Aplicado del 20% por un valor de de {valor_compra}')

# Ejercicio 3

