from kanren import run,var
from kanren import Relation,facts
M = var()
P = var()
H = var()
es_esposo_de = Relation()
facts(es_esposo_de,
		("Sabino","Rosalia"),
		("David","Flor"),
		("Rene","Nelith")
	 )
es_padre_de = Relation()
facts(es_padre_de,
		("Sabino","David"),
		("Sabino","Rene"),
		("Sabino","Hernan"),
		
		("David","Angie"),
		("Rene","Marcelo")
	 )
print("Para todo hijo hay mamá")
print(run(10,(H,M),es_padre_de(P,H),es_esposo_de(P,M)))
print("inferencia dado un hijo determina quién es la mamá")
H1 = "Marcelo"
print(run(10,M,es_padre_de(P,H1),es_esposo_de(P,M)))


