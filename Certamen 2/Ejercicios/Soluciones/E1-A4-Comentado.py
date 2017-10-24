
#encoding: utf-8
#coding: utf-8

# Ignorar lo de arriba, es sólo para poder escribir con tildes
# Definimos nuestra Base de Datos de Alumnos
Alumnos = [ ( 'Alumno 1825 ',  6  ), ( 'Alumno 7277 ',  1  ), ( 'Alumno 7652 ',  9  ), ( 'Alumno 810 ',  2  ), ( 'Alumno 7752 ',  10  ), ( 'Alumno 528 ',  8  ), ( 'Alumno 5131 ',  6  ), ( 'Alumno 3398 ',  5  ), ( 'Alumno 5796 ',  5  ), ( 'Alumno 2256 ',  8  ), ( 'Alumno 2998 ',  4  ), ( 'Alumno 3919 ',  1  ), ( 'Alumno 7365 ',  6  ), ( 'Alumno 8353 ',  10  ), ( 'Alumno 4558 ',  7  ), ( 'Alumno 1664 ',  10  ), ( 'Alumno 3504 ',  8  ), ( 'Alumno 7303 ',  3  ), ( 'Alumno 3862 ',  2  ), ( 'Alumno 3377 ',  2  ), ( 'Alumno 9407 ',  8  ), ( 'Alumno 3554 ',  5  ), ( 'Alumno 8208 ',  1  ), ( 'Alumno 9809 ',  7  ), ( 'Alumno 8643 ',  4  ), ( 'Alumno 9919 ',  10  ), ( 'Alumno 7128 ',  2  ), ( 'Alumno 3162 ',  3  ), ( 'Alumno 4825 ',  1  ), ( 'Alumno 9118 ',  5  ), ( 'Alumno 3132 ',  10  ), ( 'Alumno 3798 ',  8  ), ( 'Alumno 3508 ',  10  ), ( 'Alumno 7045 ',  1  ), ( 'Alumno 7566 ',  5  ), ( 'Alumno 6477 ',  9  ), ( 'Alumno 2067 ',  6  ), ( 'Alumno 8172 ',  4  ), ( 'Alumno 8607 ',  1  ), ( 'Alumno 391 ',  4  ), ( 'Alumno 4197 ',  7  ), ( 'Alumno 2394 ',  6  ), ( 'Alumno 2193 ',  3  ), ( 'Alumno 8099 ',  8  ), ( 'Alumno 2845 ',  1  ), ( 'Alumno 7811 ',  1  ), ( 'Alumno 2375 ',  7  ), ( 'Alumno 3608 ',  7  ), ( 'Alumno 8081 ',  3  ), ( 'Alumno 3088 ',  6  ), ( 'Alumno 1622 ',  3  ), ( 'Alumno 2227 ',  2  ), ( 'Alumno 6602 ',  2  ), ( 'Alumno 2134 ',  6  ), ( 'Alumno 6269 ',  1  ), ( 'Alumno 6662 ',  5  ), ( 'Alumno 13 ',  1  ), ( 'Alumno 6988 ',  9  ), ( 'Alumno 511 ',  5  ), ( 'Alumno 7789 ',  9  ), ( 'Alumno 353 ',  6  ), ( 'Alumno 9752 ',  10  ), ( 'Alumno 6416 ',  3  ), ( 'Alumno 6942 ',  9  ), ( 'Alumno 5992 ',  1  ), ( 'Alumno 2595 ',  3  ), ( 'Alumno 1438 ',  10  ), ( 'Alumno 2531 ',  2  ), ( 'Alumno 6282 ',  1  ), ( 'Alumno 6371 ',  6  ), ( 'Alumno 8851 ',  9  ), ( 'Alumno 2625 ',  8  ), ( 'Alumno 1794 ',  1  ), ( 'Alumno 6373 ',  10  ), ( 'Alumno 5561 ',  5  ), ( 'Alumno 465 ',  4  ), ( 'Alumno 1254 ',  4  ), ( 'Alumno 4163 ',  6  ), ( 'Alumno 8875 ',  6  ), ( 'Alumno 3738 ',  7  ), ( 'Alumno 9981 ',  3  ), ( 'Alumno 9666 ',  3  ), ( 'Alumno 2548 ',  7  ), ( 'Alumno 7887 ',  7  ), ( 'Alumno 4983 ',  10  ), ( 'Alumno 1390 ',  10  ), ( 'Alumno 1572 ',  8  ), ( 'Alumno 1238 ',  10  ), ( 'Alumno 4112 ',  5  ), ( 'Alumno 5826 ',  3  ), ( 'Alumno 4684 ',  8  ), ( 'Alumno 1605 ',  4  ), ( 'Alumno 1747 ',  4  ), ( 'Alumno 6881 ',  5  ), ( 'Alumno 7947 ',  7  ), ( 'Alumno 34 ',  2  ), ( 'Alumno 3909 ',  6  ), ( 'Alumno 9520 ',  1  ), ( 'Alumno 8460 ',  1  ), ( 'Alumno 1807 ',  7  )]
	
d = {}				# Declaramos nuestro Diccionario que tendrá los datos de los alumnos
					# Llaves: Nombres de los alumnos
					# Valores: Diccionarios con la suma de las notas, la cantidad de notas, y, el promedio

lista_final = []	# Lista que contendrá los alumnos con mayor probabilidad de reprobar ordenados por su promedio de notas.
					# Estará compuesta de tuplas (Promedio, Nombre)		

for nombre, nota in Alumnos:		# Recorremos la Base de Datos
	if nombre not in d:				# Si no está el nombre en nuestro diccionario
		d[nombre] = {}				# Definimos la llave acorde a este y le asignamos
		d[nombre]["nota"] = 0		# un diccionario que tendrá la suma de sus notas
		d[nombre]["cantidad"] = 0	# la cantidad de notas que tiene
		d[nombre]["promedio"] = 0	# y su promedio, todos en 0.

	d[nombre]["cantidad"] += 1		# Aumentamos la cantidad de notas del alumno
	d[nombre]["nota"] += nota 		# Aumentamos la suma de las notas del alumno

for nombre, datos in d.items():		# Recorremos los items de nuestro diccionario
	d[nombre]["promedio"] = datos["nota"] / datos["cantidad"]	# y calculamos el promedio de cada alumno
	
	if datos["promedio"] < 3.0:		# Si su promedio es menor a 3.0 ( Condición Reprobatoria )
		lista_final.append( ( datos["promedio"], nombre ) )		# Insertamos su promedio y nombre en la lista de tuplas que ordenaremos

lista_final.sort()												# Ordenamos la lista
																# Notar que sort() ordena en base al primer valor de cada tupla en la lista, por eso pusimos los promedios primero

print "Lista de Perones", lista_final							# Mostramos en pantalla la solución del problema.

# Ayudantías Programación de Computadores IWI-131 UTFSM 2017
# Desarrollado por Gonzalo Fernández (@DevTotal) bajo licencia MIT