
#encoding: utf-8

c = 0 		# Partidos
p = -1 		# Mayor diferencia de partidos ganados
cp = 0 		# Partido con mayor diferencia
usm = 0 	# Goles Usm
otro = 0	# Goles Otro
Tusm = 0 	# Goles Total USm
Totro = 0 	# Goles Total Otro
v = 0		# Victorias Continua
dif1 = 0	# Diferencia último partido
dif2 = 0	# Diferencia penultimo partido

a = int(raw_input("Opcion"))

while a != 0:
	if a == 1:
		usm = int(raw_input("USM:"))
		otro = int(raw_input("Otro:"))
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
				print "Racha Superada, sos tremendo papá"
		else:
			if v >= 3:
				print "Uff, la perdiste papá, sos un pibe viejo"
			v = 0

	elif a == 2:
		if c > 0:
			print usm, otro
		else:
			print "No hay informacion"
	elif a == 3:
		if c > 0:
			print cp
		else:
			print "No hay informacion"

	elif a == 4:
		if c > 0:
			print Tusm / c, c
		else:
			print "No hay informacion"
	else:
		print "Opcion No Valida"
	
	a = int(raw_input("Opcion: "))

if c >= 2:
	if dif1 < 0 and dif2 < 0:
		print "Rendimiento tiende a 0"
	elif dif1 > 0 and dif2 > 0:
		print "Rendimiento bonito"
	else:
		print "Rendimiento regular"
else:
	print "No hay informacion"