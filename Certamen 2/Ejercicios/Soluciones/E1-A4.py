
Alumnos = [ ( 'Alumno 1825 ',  6  ), ( 'Alumno 7277 ',  1  ), ( 'Alumno 7652 ',  9  ), ( 'Alumno 810 ',  2  ), ( 'Alumno 7752 ',  10  ), ( 'Alumno 528 ',  8  ), ( 'Alumno 5131 ',  6  ), ( 'Alumno 3398 ',  5  ), ( 'Alumno 5796 ',  5  ), ( 'Alumno 2256 ',  8  ), ( 'Alumno 2998 ',  4  ), ( 'Alumno 3919 ',  1  ), ( 'Alumno 7365 ',  6  ), ( 'Alumno 8353 ',  10  ), ( 'Alumno 4558 ',  7  ), ( 'Alumno 1664 ',  10  ), ( 'Alumno 3504 ',  8  ), ( 'Alumno 7303 ',  3  ), ( 'Alumno 3862 ',  2  ), ( 'Alumno 3377 ',  2  ), ( 'Alumno 9407 ',  8  ), ( 'Alumno 3554 ',  5  ), ( 'Alumno 8208 ',  1  ), ( 'Alumno 9809 ',  7  ), ( 'Alumno 8643 ',  4  ), ( 'Alumno 9919 ',  10  ), ( 'Alumno 7128 ',  2  ), ( 'Alumno 3162 ',  3  ), ( 'Alumno 4825 ',  1  ), ( 'Alumno 9118 ',  5  ), ( 'Alumno 3132 ',  10  ), ( 'Alumno 3798 ',  8  ), ( 'Alumno 3508 ',  10  ), ( 'Alumno 7045 ',  1  ), ( 'Alumno 7566 ',  5  ), ( 'Alumno 6477 ',  9  ), ( 'Alumno 2067 ',  6  ), ( 'Alumno 8172 ',  4  ), ( 'Alumno 8607 ',  1  ), ( 'Alumno 391 ',  4  ), ( 'Alumno 4197 ',  7  ), ( 'Alumno 2394 ',  6  ), ( 'Alumno 2193 ',  3  ), ( 'Alumno 8099 ',  8  ), ( 'Alumno 2845 ',  1  ), ( 'Alumno 7811 ',  1  ), ( 'Alumno 2375 ',  7  ), ( 'Alumno 3608 ',  7  ), ( 'Alumno 8081 ',  3  ), ( 'Alumno 3088 ',  6  ), ( 'Alumno 1622 ',  3  ), ( 'Alumno 2227 ',  2  ), ( 'Alumno 6602 ',  2  ), ( 'Alumno 2134 ',  6  ), ( 'Alumno 6269 ',  1  ), ( 'Alumno 6662 ',  5  ), ( 'Alumno 13 ',  1  ), ( 'Alumno 6988 ',  9  ), ( 'Alumno 511 ',  5  ), ( 'Alumno 7789 ',  9  ), ( 'Alumno 353 ',  6  ), ( 'Alumno 9752 ',  10  ), ( 'Alumno 6416 ',  3  ), ( 'Alumno 6942 ',  9  ), ( 'Alumno 5992 ',  1  ), ( 'Alumno 2595 ',  3  ), ( 'Alumno 1438 ',  10  ), ( 'Alumno 2531 ',  2  ), ( 'Alumno 6282 ',  1  ), ( 'Alumno 6371 ',  6  ), ( 'Alumno 8851 ',  9  ), ( 'Alumno 2625 ',  8  ), ( 'Alumno 1794 ',  1  ), ( 'Alumno 6373 ',  10  ), ( 'Alumno 5561 ',  5  ), ( 'Alumno 465 ',  4  ), ( 'Alumno 1254 ',  4  ), ( 'Alumno 4163 ',  6  ), ( 'Alumno 8875 ',  6  ), ( 'Alumno 3738 ',  7  ), ( 'Alumno 9981 ',  3  ), ( 'Alumno 9666 ',  3  ), ( 'Alumno 2548 ',  7  ), ( 'Alumno 7887 ',  7  ), ( 'Alumno 4983 ',  10  ), ( 'Alumno 1390 ',  10  ), ( 'Alumno 1572 ',  8  ), ( 'Alumno 1238 ',  10  ), ( 'Alumno 4112 ',  5  ), ( 'Alumno 5826 ',  3  ), ( 'Alumno 4684 ',  8  ), ( 'Alumno 1605 ',  4  ), ( 'Alumno 1747 ',  4  ), ( 'Alumno 6881 ',  5  ), ( 'Alumno 7947 ',  7  ), ( 'Alumno 34 ',  2  ), ( 'Alumno 3909 ',  6  ), ( 'Alumno 9520 ',  1  ), ( 'Alumno 8460 ',  1  ), ( 'Alumno 1807 ',  7  )]
	
d = {}				
lista_final = []	
for nombre, nota in Alumnos:	
	if nombre not in d:			
		d[nombre] = {}			
		d[nombre]["nota"] = 0	
		d[nombre]["cantidad"] = 0
		d[nombre]["promedio"] = 0

	d[nombre]["cantidad"] += 1	
	d[nombre]["nota"] += nota 	

for nombre, datos in d.items():	
	d[nombre]["promedio"] = datos["nota"] / datos["cantidad"]	
	
	if datos["promedio"] < 3.0:
		lista_final.append( ( datos["promedio"], nombre ) )		

lista_final.sort()
print "Lista de Perones", lista_final