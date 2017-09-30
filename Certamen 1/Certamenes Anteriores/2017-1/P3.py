
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

	if c1 == meta:	
		return 1	
					
	if c2 == meta:	
		return 2	
					
	if c3 == meta:	
		return 3	
					
	return 0		

def contar(palabra):
	
	vocales = 0		 

	for i in palabra: 
		if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
			vocales += 1	

	return vocales	 

def final():

	meta = int(raw_input("Ingrese la meta del Juego: ")) 

	c1 = 0 				
	c2 = 0 				
	c3 = 0 				
	palabra1 = "" 		
	palabra2 = "" 		
	palabra3 = "" 		
	maximo = 0			
	maximo_alianza = 0	

	while ganador(c1, c2, c3, meta) == 0: 	

		palabra1 = raw_input("alianza 1: ")	
		maximo = contar(palabra1)			
		maximo_alianza = 1					

		palabra2 = raw_input("alianza 2: ")	

		if maximo < contar(palabra2):		
			maximo = contar(palabra2)		
			maximo_alianza = 2				

		palabra3 = raw_input("alianza 3: ")	

		if maximo < contar(palabra3):		
			maximo = contar(palabra3)		
			maximo_alianza = 3				

		if maximo == contar(palabra1) and maximo == contar(palabra2) or maximo == contar(palabra1) and maximo == contar(palabra3) or maximo == contar(palabra2) and maximo == contar(palabra3):
			continue

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