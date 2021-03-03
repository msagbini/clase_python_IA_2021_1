# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 22:34:24 2021

@author: RYZEN
"""
# Ejercicio 1
persona1 = float(input("Digite el valor que invertió la persona 1"))
persona2 = float(input("Digite el valor que invertió la persona 2"))
persona3 = float(input("Digite el valor que invertió la persona 3"))
c_invertida = persona1 + persona2 + persona3


# Ejercicio 2
sueldo_base = float(input("¿Cuánto es su sueldo base?: "))
c_hijos = int(input("¿Cuántos hijos tiene?: "))
bonificacion = c_hijos * 80000
total = bonificacion + sueldo_base
print(f"Su bonificación es de: {bonificacion} y el sueldo total: {total}")

# Ejercicio 3
monto_ahorrado = float(input("Digite su monto ahorrado"))
saldo_final = monto_ahorrado * 1.015
print(f"Su saldo final es de: {saldo_final}")

# Ejercicio 4
v_metrocuadrado = float(input("Digite cuántos metros cuadrados desea: "))
valor_terreno = v_metrocuadrado * 80000
cuota_inicial = valor_terreno * 0.35
valor_cuotas = (valor_terreno*0.65)/12
print(f"La cuota inicial es de {cuota_inicial} y el valor por cuota es de {valor_cuotas}")

# Ejercicio 5
sueldo = float(input("Digite su sueldo: "))
imp_ley = sueldo * 0.01
imp_seguro = sueldo * 0.04
imp_forzoso = sueldo * 0.005
ahorro = sueldo * 0.05
valor_pagar = sueldo * 0.895
print(f"El impuesto por ley pública es de: {imp_ley}")
print(f"El valor descontado por seguro es de {imp_seguro}")
print(f"El valor descontado por seguro forzoso es de {imp_forzoso}")
print(f"El valor descontado por caja de ahorro es de {ahorro}")
print(f"El sueldo total es de: {valor_pagar} ")

# Ejercicio 6
print("Bienvenido al periódico el informador.")
c_palabra = float(input("Digite la cantidad de palabras de su anuncio: "))
c_cms = float(input("Digite la cantidad de centímetros de su anuncio: "))
c_colores = float(input("Digite la cantidad de colores de su anuncio: "))
v_anuncio = (c_palabra * 20000) + (c_cms * 15000) + (c_colores * 25000)
print(f"El valor total de su anuncio es de {v_anuncio}")

# Ejercicio 7
años_laborados = int(input("Digite cuántos años ha laborado: "))
bono = 100000 + ((años_laborados-1) * 120000)
print(f"El valor del bono es de {bono}")

# Ejercicio 8
h_trabajadas = int(input("Digite la cantidad de horas trabajadas: "))
v_horas = h_trabajadas * 20000
descuento = v_horas * 0.05
v_total = v_horas - descuento
print(f"El valor del descuento es: {descuento} y el valor a pagar es: {v_total}")

#Ejercicio 9
monto_inicial = float(input("Digite el monto inicial de la tarjeta"))