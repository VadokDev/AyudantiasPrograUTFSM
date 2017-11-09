M = {  
	
	"O" : { 
		1 : ["Asd", "Queremos", 1],
		0 : ["Humanos", "s"],
		5 : ["Asd", 1, 4, [], "as", "Decirles"],
	    "C" : ( set("59s"), set("aks4") )
	  },
	    "s" : {
		6 : ["", 1, 2, 3, 1, 3, "AL Oido"],
	    "C" : ( set("asd42"), set("dm3ia") )
	  },
	    "X" : {
		3 : [ 0, 12, "LoL", "U Cuitoh en Maincra","rule"],
		"C" : ( set("Nand Kore"), set("Wa") ),
	  },
	   "a" : {
		0 : ["Tantas", 0, [2], {4 : 5}, {1, 2, 3}, "34"],
		9 : ["Cos", "C", 12, 2, 1, 2, 3, 9,  9, "Cosa Preciosas"]
	}
}

def descifrar(M, L):
	
	mensaje = ""
	while "C" in M[L]:
		llaves = M[L].keys()
		llaves.remove("C")
		llaves.sort()
		for i in llaves:
			mensaje += M[L][i][i]+" "

		c1 = M[L]["C"][0]
		c2 = M[L]["C"][1]
		c = c1 & c2
		L = list(c)[0]

	llaves = M[L].keys()
	llaves.sort()
	for i in llaves:
		mensaje += M[L][i][i]+" "

	print mensaje

descifrar(M, "O")