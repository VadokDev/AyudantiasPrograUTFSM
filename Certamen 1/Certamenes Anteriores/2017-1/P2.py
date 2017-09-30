#coding: utf-8
#encoding: utf-8

def pregunta1():

	s1 = 0
	s2 = 0
	s3 = 0
	m1 = 0
	m2 = 0
	m3 = 0
	a1 = 0
	a2 = 0
	a3 = 0
	Precio = 0

	Area = 	 int( raw_input("Ingrese el Area: ") )

	if Area > 0:
		Sector = int( raw_input("Ingrese el Sector: ") )

	while Area > 0:

		Precio = 20 * Area
		if Area < 100:
			Precio = Precio - Precio * 0.1
		elif Area <= 1000:
			Precio = Precio * 1.2
		else:
			Precio = Precio + (Precio * 0.5)

		if Sector == 1:
			s1 += Precio
			if Precio > m1:
				m1 = Precio
				a1 = Area
		elif Sector == 2:
			s2 += Precio
			if Precio > m2:
				m2 = Precio
				a2 = Area
		else:
			s3 += Precio
			if Precio > m3:
				m3 = Precio
				a3 = Area

		Area = 	 int( raw_input("Ingrese el Area: ") )

		if Area > 0:
			Sector = int( raw_input("Ingrese el Sector: ") )

	
	print "Sector 1:"
	print "\tValor Total: $", s1
	print "\tValor y Área del Terreno más caro: $",m1,"y",a1,"m^2\n"

	print "Sector 2:"
	print "\tValor Total: $", s2
	print "\tValor y Área del Terreno más caro: $",m2,"y",a2,"m^2\n"

	print "Sector 3:"
	print "\tValor Total: $", s3
	print "\tValor y Área del Terreno más caro: $",m3,"y",a3,"m^2\n"

pregunta1()

# Ayudantías Programación de Computadores IWI-131 UTFSM 2017
# Desarrollado por Gonzalo Fernández (@DevTotal) bajo licencia MIT