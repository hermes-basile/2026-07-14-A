import copy

import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self.all_director = DAO.getAllDirector()
        self.idMapObject = {}
        for nodo in self.all_director:
            self.idMapObject[nodo.id] = nodo





    def crea_grafo(self, dataInizio, dataFine):
        self._grafo.clear()
        #nodi
        lista_nodi = []
        lista_id_nodi = DAO.getDirectorNodes(dataInizio, dataFine)

        for id_direttore in lista_id_nodi:
            lista_nodi.append(self.idMapObject[id_direttore])
            DAO.getAllInfoFilm(self.idMapObject[id_direttore], dataInizio, dataFine)

        self._grafo.add_nodes_from(lista_nodi)


        #archi
        self.add_archi(dataInizio, dataFine)


    def add_archi(self, dataInizio, dataFine):
        lista_idDirector_idGenre = DAO.getDirectorGenre(dataInizio, dataFine)
        dizionarioDirectorGenre = {}

        for director_id,genre in lista_idDirector_idGenre:
            if director_id not in dizionarioDirectorGenre.keys():
                dizionarioDirectorGenre[director_id] = set()
            dizionarioDirectorGenre[director_id].add(genre)
        lista_direttori = list(dizionarioDirectorGenre.keys())
        for i in range (0,len(lista_direttori)):
            for j in range (i +1 ,len(lista_direttori)):
                direttore1 = self.idMapObject[lista_direttori[i]]
                direttore2 = self.idMapObject[lista_direttori[j]]
                numero_comuni = self.numero_generi_comuni(direttore1,direttore2,dizionarioDirectorGenre)
                if numero_comuni > 0:
                    self._grafo.add_edge(direttore1,direttore2,peso= numero_comuni)




    def numero_generi_comuni(self, direttore1, direttore2, dizionario):
        set1 = dizionario[direttore1.id]
        set2 = dizionario[direttore2.id]
        set_comuni = set1 & set2
        return len(set_comuni)


    def regista_grado_maggiore(self):
        maggiore = 0
        nodo_salvato = None
        if len(list(self._grafo.nodes)) > 0:
            for nodo in list(self._grafo.nodes):
                grado = self._grafo.degree(nodo)
                if grado > maggiore:
                    maggiore = grado
                    nodo_salvato = nodo
        return nodo_salvato, maggiore

    def regista_peso_maggiore(self):
        lista_nodi = list(self._grafo.nodes)
        peso_salvato = 0
        direttore_salvato = None
        if len(lista_nodi) > 0 :
            for nodo in lista_nodi:
                peso_totale = self._grafo.degree(nodo, weight="peso")
                if peso_totale > peso_salvato:
                    peso_salvato = peso_totale
                    direttore_salvato = nodo
        return direttore_salvato,peso_salvato

    def cinque_archi_peso_maggiore(self):
        lista_archi = list(self._grafo.edges(data=True))
        lista_ordinata = sorted(lista_archi, key=lambda tupla: (-tupla[2]["peso"],tupla[0].name,tupla[1].name))
        return lista_ordinata[:5]

    def crea_albero(self, source, N):
        self.soluzione = []
        self.incasso_salvato = 0

        self.ricorsione([source], N)
        return self.soluzione


    def ricorsione(self, parziale, N):

        if len(parziale) == N and self.incasso_totale_lista(parziale) > self.incasso_salvato:
            self.soluzione = copy.deepcopy(parziale)
            self.incasso_salvato = self.incasso_totale_lista(parziale)
            return

        for direttore in list(self._grafo.nodes()):
            if self.is_ammissibile(direttore, parziale):
                parziale.append(direttore)
                self.ricorsione(parziale, N)
                parziale.pop()




    def is_ammissibile(self, possibile, parziale):
        for nodo_presente in parziale:
            if (self._grafo.has_edge(possibile, nodo_presente)

                    and possibile not in parziale):
                return True
        return False

    def incasso_totale_lista(self, lista):
        incasso_lista = 0
        if len(lista)>0:
            for direttore in lista:
                incasso_direttore = direttore.calcola_tot_income()
                incasso_lista += incasso_direttore
        return incasso_lista



    def num_nodi(self):
        return len(self._grafo.nodes)

    def num_archi(self):
        return len(self._grafo.edges)
