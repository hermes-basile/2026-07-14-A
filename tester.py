from model.model import Model
from model.regista import Regista
modello_prova = Model()

#print(modello_prova.all_director)
#rint(modello_prova.crea_grafo("2017-01-01","2019-01-01")) "2017-01-01" "2019-12-31"
modello_prova.crea_grafo("2017-01-01","2019-12-31")
print(modello_prova.num_nodi())
print(modello_prova.num_archi())
#print(modello_prova.regista_grado_maggiore())
#print(modello_prova.regista_peso_maggiore())
#print(modello_prova.cinque_archi_peso_maggiore())
#print((modello_prova.cinque_archi_peso_maggiore()))
direttore1 = modello_prova.regista_grado_maggiore()
print(modello_prova.regista_grado_maggiore())
print(modello_prova.crea_albero(direttore1[0],2))
#print(direttore1[0].calcola_tot_income())
print(modello_prova.incasso_totale_lista())

