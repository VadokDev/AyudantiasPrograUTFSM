
#encoding: utf-8
#Recuerden, esto de arriba sólo es para poder comentar con tildes, no tiene ninguna otra particularidad

c = 0 		# Total de partidos jugados
p = -1 		# Mayor diferencia obtenida en un partido
cp = 0 		# Partido en el que se obtuvo la mayor diferencia
usm = 0 	# Goles del último partido de la USM
otro = 0	# Goles del último partido de Otro
Tusm = 0 	# Goles realizados en total por USM
Totro = 0 	# Goles realizados en total por Otro
v = 0		# Victorias consecutivas realizadas por la USM
dif1 = 0	# Diferencia de goles del último partido
dif2 = 0	# Diferencia de goles del penúltimo partido

a = int(raw_input("Operación?: ")) # Solicitamos la primera operación a realizar y la pasamos a int para poder usarla más cómodamente en las condiciones

while a != 0:	# Ejecutamos este while mientras la opción ingresada no sea 0
	if a == 1:									# Si la opción ingresada es 1
		usm = int(raw_input("Goles USM: "))		# Solicitamos los goles de la USM y y los pasamos a int para así no guardar strings
		otro = int(raw_input("Goles Otro: "))	# Solicitamos los goles de Otro y y los pasamos a int para así no guardar strings
		Tusm += usm 							# Aumentamos la cantidad de goles total de la USM
		Totro += otro 							# Aumentamos la cantidad de goles total de Otro
		c += 1									# Aumentamos la cantidad de partidos
		
		dif2 = dif1								# Guardamos la penúltima diferencia de goles
		dif1 = usm - otro 						# Guardamos la última diferencia de goles
												# Asuman que el partido ingresado es siempre el último

		if usm - otro > p:						# Si la diferencia de goles de este partido es mayor a la anterior mayor diferencia
			p = usm - otro 						# Guardamos esta mayor diferencia
			cp = c 								# Guardamos el partido en que se registró esta mayor diferencia

		if usm > otro: 							# Si la USM realizó más goles que Otro
			v += 1 								# Aumenta la cantidad de victorias
			if v % 3 == 0:						# Si ha realizado una cantidad de victorias múltiplo de 3
				print "**Enhorabuena has batido el record**"	# Anunciamos que ha batido un record
		else:									# En caso de que la USM haya perdido
			if v >= 3:							# Sólo si tiene una racha ganadora (más de 3 victorias seguidas)
				print "** Fin de la racha ganadora **"	# Mostramos el aviso de que perdió la racha
			v = 0								# Reiniciamos la cantidad de victorias consecutivas, pues, perdió

	elif a == 2:								# Si la opción ingresada es la 2
		if c > 0:								# En caso de haber información (si ya se han ingresado partidos)
			print "USM", usm, "v/s", "Otro", otro # Mostramos el marcador del último partido
		else:									# En caso de no haber información
			print "** No existe información disponible **" # Alertamos como el enunciado nos pide

	elif a == 3:								# Si la opción ingresada es la 3
		if c > 0:								# En caso de haber información (si ya se han ingresado partidos)
			print "El partido con mejor diferencia de goles es el ", cp # Mostramos el partido donde se registró la mayor diferencia de goles a favor
		else:									# En caso de no haber información
			print "** No existe información disponible **" # Alertamos como el enunciado nos pide

	elif a == 4:								# Si la opción ingresada es la 4
		if c > 0:								# En caso de haber información (si ya se han ingresado partidos)
			print "Promedio Goles:", float(Tusm) / float(c), "en", c, "partidos" # Indicamos el promedio de goles y la cantidad de partidos considerados
						# OJO, al menos 1 de los 2 elementos de esta división debe ser float, de modo que el resultado sea float también (entiéndase, el resultado contenga sus decimales)
						# De lo contrario, esta división devolverá el valor redondeado, sin decimales
		else:			# En caso de no haber información
			print "** No existe información disponible **" # Alertamos como el enunciado nos pide

	else:				# En caso de que la opción ingresada no sea ni la 1, 2, 3, 4 (sabemos que no es la 0 porque de ser así no se ejecutaría el while)
		print "La operación no existe"	# Indicamos que la operación no existe como el enunciado nos pide
	
	print ""			# Este print es nétamente de adorno, sirve para poner un salto de línea después de la opción ingresada y hacer que el programa se vea igual que el ejemplo del enunciado
	a = int(raw_input("Operación?: : "))	# Volvemos a solicitar una opción al usuario, ESTA PARTE ES SÚPER IMPORTANTE

if c >= 2:											# Si existen 2 partidos de los cuales extraer la información solicitada
	if dif1 < 0 and dif2 < 0:						# Comprobamos si las diferencias en el último y penúltimo partido son menores a 0, lo que significa que perdió ambos partidos
		print "Su rendimiento está bajando"			# De perder ambos partidos, indicamos que el rendimiento está bajando
	elif dif1 > 0 and dif2 > 0:						# # Comprobamos si las diferencias en el último y penúltimo partido son menores a 0, lo que significa que perdió ambos partidos
		print "Su rendimiento está subiendo"		# De ganar ambos partidos, indicamos que el rendimiento está subiendo
	else:											# En caso de no ganar ambos partidos ni perder ambos partidos (esto es, básicamente, haber perdido 1 y ganado 1, ó, haber empatado ambos)
		print "Su rendimiento es regular"			# Indicamos que el rendimiento es regular
else:												# Si no existen 2 partidos de los cuales extraer la información
	print "** No existe información disponible **"	# Alertamos como indica el enunciado

print "Adiós" 	# Otro print puesto para que el programa se parezca al ejemplo del enunciado