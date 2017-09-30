
#encoding: utf-8
#coding: utf-8

# Ignorar lo de arriba, es sólo para poder escribir con tildes
# Análisis del Problema:
# 
# *Nota - La función C) no especifica un nombre, así que le 
#         llamaremos C) en este Análisis y final() en el código
#
# Valores:
# 
# 	- Existen 3 alianzas
# 	- Existe una serie limitada de turnos
# 	- Sólo 1 alianza gana
# 
# Datos de Entrada:
# 	
# 	* Función ganador:
# 		- c1, c2, c3: Cantidad de juegos ganados por cada alianza.
# 		- meta: Meta a lograr en el juego
# 
# 	* Función contar:
# 		- palabra: Palabra ingresada por una alianza
# 
# 	* Función C):
# 		- meta: Meta a lograr en el juego
# 		- palabras: Palabras de cada alianza por turno
# 
# Condiciones Explícitas:
# 
# 	* Generales:
# 		- En cada turno cada alianza ingresa una palabra
# 		- Gana la alianza que ingrese la palabra con más vocales
# 		- Si 2 o más alianzas empatan en la cantidad de vocales MÁXIMA de la palabra, nadie gana (si 2 o más empatan en la mayor cantidad de vocales)
# 		- El concurso acaba cuando una alianza gana X juegos, donde x es la meta y se define al inicio
# 
# 	* Función ganador:
# 		- No existen empates al momento de alcanzar la meta
# 		- De no existir ganador, retornar 0
# 
# 	* Función contar:
# 		- No se puede usar el método count
# 
# 	* Función C):
# 		- Se deben solicitar palabras hasta que una alianza gane
# 
# Datos de Salida:
# 
# 	* Función ganador:
# 		- Número de la alianza ganadora, ó, 0 en caso de que nadie gane
# 
# 	* Función contar:
# 		- Cantidad de vocales de la palabra
# 
# 	* Función C):
# 		- Alianza ganadora

def ganador(c1, c2, c3, meta):

	if c1 == meta:	# Dato que existe la condición explícita 
		return 1	# de que no existirán empates al momento
					# de alcanzar la meta, podemos resolver
	if c2 == meta:	# este problema comprobando diréctamente
		return 2	# si alguna alianza llegó a la meta
					# y devolver el número de esta
	if c3 == meta:	# en caso de que ninguna alianza
		return 3	# haya completado el número de victorias
					# necesarias para ganar, entonces se asume
	return 0		# que nadie ganó y devolvemos 0

def contar(palabra):
	
	vocales = 0		  # Inicializamos la variable vocales que contendrá las vocales de la palabra

	for i in palabra: # Recorremos cada caracter del string palabra
		if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
			vocales += 1	# Si el caracter es una vocal, aumentamos la variable vocales

	return vocales	  # Devolvemos el resultado solicitado

def final():

	meta = int(raw_input("Ingrese la meta del Juego: ")) # Almacenamos la meta del juego

	c1 = 0 				# Victorias de la Alianza 1
	c2 = 0 				# Victorias de la Alianza 2
	c3 = 0 				# Victorias de la Alianza 3
	palabra1 = "" 		# Variable que almacenará la palabra ingresada por la Alianza 1 en su turno
	palabra2 = "" 		# Variable que almacenará la palabra ingresada por la Alianza 2 en su turno
	palabra3 = "" 		# Variable que almacenará la palabra ingresada por la Alianza 3 en su turno
	maximo = 0			# Variable que almacenará la cantidad máxima de vocales de la ronda
	maximo_alianza = 0	# Variable que almacenará la alianza que ingresó la mayou cantidad de vocales de la ronda

	while ganador(c1, c2, c3, meta) == 0: 	# Mientras no exista un ganador

		palabra1 = raw_input("alianza 1: ")	# Solicitamos la palabra de la Alianza 1
		maximo = contar(palabra1)			# En un principio asumiremos que la Alianza 1
		maximo_alianza = 1					# ingresó la palabra con el máximo de vocales

		palabra2 = raw_input("alianza 2: ")	# Solicitamos la palabra de la Alianza 2

		if maximo < contar(palabra2):		# Si la Alianza 2 ingresó una palabra con
			maximo = contar(palabra2)		# más vocales que la Alianza 1, hacemos
			maximo_alianza = 2				# el cambio en las variables maximo y maximo_alianza

		palabra3 = raw_input("alianza 3: ")	# Solicitamos la palabra de la Alianza 3

		if maximo < contar(palabra3):		# Si la Alianza 3 ingresó una palabra con
			maximo = contar(palabra3)		# más vocales que la Alianza 2, hacemos
			maximo_alianza = 3				# el cambio en las variables maximo y maximo_alianza

		# Realizado esto, en las variables maximo y maximo_alianza tendríamos el máximo de vocales ingresado y la alianza que lo ingresó

		if maximo == contar(palabra1) and maximo == contar(palabra2) or maximo == contar(palabra1) and maximo == contar(palabra3) or maximo == contar(palabra2) and maximo == contar(palabra3):
			continue	# Si más de una alianza alcanza el máximo de vocales, nadie gana, por ende, nos saltamos la ronda
		
		# Finalmente, si no hubo empate, asignamos la victoria a la alianza correspondiente

		if maximo_alianza == 1:
			c1 += 1
		elif maximo_alianza == 2:
			c2 += 1
		else:
			c3 += 1

	print "La alianza ganadora es:", ganador(c1, c2, c3, meta)

final()

# Ayudantías Programación de Computadores IWI-131 UTFSM 2017
# Desarrollado por Gonzalo Fernández (@DevTotal) bajo licencia MIT