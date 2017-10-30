
misiles = { '201Uk' : (800, 20), '22kVB' : (1000, 5), 'Uk312' : (10, 100) }
barcos = { 'USS Enterprise' : (130, 200), 'USS Barack' : (100, -50), 'US Barack' : (1, -50) }

def distancia(x, y):
	return (x**2 + y**2)**0.5

def distancia_dos(x1, y1, x2, y2):
	return ((x2-x1)**2 + (y2-y1)**2)**0.5

def vector_unitario(x, y):
	return 1 / distancia(x, y)

def distancia_maxima(x, y, alcance):
	v = vector_unitario(x, y)
	return (x * v * alcance, y * v * alcance)

def panic(misiles, barcos):

	lista_orden = []
	resultado = {}

	for x, y in barcos.values():
		lista_orden.append( [distancia(x, y), x, y, 0] )

	lista_orden.sort()
	lista_orden.reverse()
	lista_misiles = []

	for i in misiles.items():
		misiles[i[0]] = list(misiles[i[0]])
		misiles[i[0]].append(i[0])
		misiles[i[0]].append(0)
		lista_misiles.append(misiles[i[0]])

	for i in range(len(lista_misiles)):
		for j in range(len(lista_orden)):
			dx, dy = distancia_maxima(lista_orden[j][1], lista_orden[j][2], lista_misiles[i][0])
			
			if lista_misiles[i][3] == 1 or lista_orden[j][3] == 1:
				continue

			if distancia_dos(lista_orden[j][1], lista_orden[j][2], dx, dy) <= lista_misiles[j][1]:

				resultado[lista_misiles[i][2]] = (lista_orden[j][1], lista_orden[j][2])
				lista_misiles[i][3] = 1
				lista_orden[j][3] = 1
				break
			elif distancia(lista_orden[j][1], lista_orden[j][2]) <= lista_misiles[j][0]:
				lista_misiles[i][3] = 1
				lista_orden[j][3] = 1
				resultado[lista_misiles[i][2]] = (lista_orden[j][1], lista_orden[j][2])
				break

	return resultado

print panic(misiles, barcos)
