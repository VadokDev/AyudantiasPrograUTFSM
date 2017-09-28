
#encoding: utf-8
#coding: utf-8

# Ignorar lo de arriba, es sólo para poder escribir con tildes

def pregunta1():	# Definimos la función que resolverá nuestro problema
	
	# Declaramos las variables con las que trabajaremos

	s1 = 0			# Precio total del sector 1
	s2 = 0			# Precio total del sector 2
	s3 = 0			# Precio total del sector 3
	m1 = 0			# Precio del terreno más caro del sector 1
	m2 = 0			# Precio del terreno más caro del sector 2
	m3 = 0			# Precio del terreno más caro del sector 3
	a1 = 0			# Área del terreno más caro del sector 1
	a2 = 0			# Área del terreno más caro del sector 2
	a3 = 0			# Área del terreno más caro del sector 3

	Precio = 0		# Precio del terreno ingresado

	Area = int( raw_input("Ingrese el Area: ") )			# Leemos el primer Área del terreno ingresado

	if Area > 0:											# En caso de ser 0, no solicitamos el Sector
		Sector = int( raw_input("Ingrese el Sector: ") )	# Leemos el Sector al que corresponde el Área anterior

	while Area > 0:	# Mientras el Área ingresada sea mayor que 0 (mientras no sea 0, también es válido Area != 0)

		# Cálculo del valor total del Área del terreno ingresado

		Precio = 20 * Area					 # Precio base del terreno
		if Area < 100:						 # Sí el Área del terreno es mayor a 100m^2
			Precio = Precio - Precio * 0.1	 # entonces le descontamos el 10%

		elif Area <= 1000:					 # Si el Área está entre 100 y 1000 m^2
			Precio = Precio * 1.2			 # entonces le agregamos el 20%

		else:								 # Por último, si el Área es mayor a 1000 m^2
			Precio = Precio + (Precio * 0.5) # le sumamos el 50% al precio

		# Identificar a qué Sector sumarle el Precio y determinación del Área y Precio del terreno más caro

		if Sector == 1:			# Si el Sector ingresado es el 1
			s1 += Precio 		# se le agrega el precio del terreno ingresado
			if Precio > m1:		# y en caso de ser mayor que el Precio del terreno más caro actual del Sector
				m1 = Precio 	# se almacena el nuevo Precio del terreno más caro
				a1 = Area 		# y el Área del mismo

		elif Sector == 2: 		# Si el Sector ingresado es el 1
			s2 += Precio 		# se le agrega el precio del terreno ingresado
			if Precio > m2: 	# y en caso de ser mayor que el Precio del terreno más caro actual del Sector
				m2 = Precio 	# se almacena el nuevo Precio del terreno más caro
				a2 = Area 		# y el Área del mismo

		else:					# Si el Sector ingresado es el 1
			s3 += Precio 		# se le agrega el precio del terreno ingresado
			if Precio > m3: 	# y en caso de ser mayor que el Precio del terreno más caro actual del Sector
				m3 = Precio 	# se almacena el nuevo Precio del terreno más caro
				a3 = Area 		# y el Área del mismo

		Area = int( raw_input("Ingrese el Area: ") )			# Leemos el primer Área del terreno ingresado

		if Area > 0:											# En caso de ser 0, no solicitamos el Sector
			Sector = int( raw_input("Ingrese el Sector: ") )	# Leemos el Sector al que corresponde el Área anterior


	print "Sector 1:"
	print "\tValor Total: $", s1
	print "\tValor y Área del Terreno más caro: $",m1,"y",a1,"m^2\n"

	print "Sector 2:"
	print "\tValor Total: $", s2
	print "\tValor y Área del Terreno más caro: $",m2,"y",a2,"m^2\n"

	print "Sector 3:"
	print "\tValor Total: $", s3
	print "\tValor y Área del Terreno más caro: $",m3,"y",a3,"m^2\n"

	# Notas:
	#	\t es un "TAB" al momento de printear
	#	\n es un "Salto de Línea" al momento de printear

pregunta1()	# Llamamos a la función que declaramos anteriormente

# Ayudantías Programación de Computadores IWI-131 UTFSM 2017
# Desarrollado por Gonzalo Fernández bajo licencia MIT