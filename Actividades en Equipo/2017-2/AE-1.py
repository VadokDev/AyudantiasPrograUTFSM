
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

a = int(raw_input("Operación?: "))

while a != 0:
	if a == 1:
		usm = int(raw_input("Goles USM: "))
		otro = int(raw_input("Goles Otro: "))
		Tusm += usm
		Totro += otro
		c += 1
		
		dif2 = dif1
		dif1 = usm - otro

		if usm - otro > p:
			p = usm - otro
			cp = c

		if usm > otro:
			v += 1
			if v % 3 == 0:
				print "**Enhorabuena has batido el record**"
		else:
			if v >= 3:
				print "** Fin de la racha ganadora **"
			v = 0

	elif a == 2:
		if c > 0:
			print "USM", usm, "v/s", "Otro", otro
		else:
			print "** No existe información disponible **"
	elif a == 3:
		if c > 0:
			print "El partido con mejor diferencia de goles es el ", cp
		else:
			print "** No existe información disponible **"

	elif a == 4:
		if c > 0:
			print "Promedio Goles:", float(Tusm) / float(c), "en", c, "partidos"
		else:
			print "** No existe información disponible **"
	else:
		print "La operación no existe"
	
	print ""
	a = int(raw_input("Operación?: : "))

if c >= 2:
	if dif1 < 0 and dif2 < 0:
		print "Su rendimiento está subiendo"
	elif dif1 > 0 and dif2 > 0:
		print "Su rendimiento está bajando"
	else:
		print "Su rendimiento es regular"
else:
	print "** No existe información disponible **"

print "Adiós"