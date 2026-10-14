import flet as ft


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def handleCreaGrafo(self, e):
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text("Stiamo creando il grafo attendi qualche secondo.."))
        self._view.update_page()
        dataInizio = self._view._dpFrom.value
        dataFine = self._view._dpTo.value
        if dataInizio is not None and dataFine is not None:
            self._model.crea_grafo(dataInizio, dataFine)
            self._view._txt_result.controls.clear()

            self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato", color="green"))
            self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.num_nodi()} nodi e {self._model.num_archi()} archi"))
        else:
            self._view._txt_result.controls.append(ft.Text("Devi selezionare correttamente le 2 date", color="red"))

        self._view.update_page()



    def handleStampaInfo(self, e):
        self._view._txt_result.controls.clear()
        nodo_maggiore, grado_maggiore = self._model.regista_grado_maggiore()
        nodo_massimo, peso_massimo = self._model.regista_peso_maggiore()




        self._view._txt_result.controls.append(ft.Text(f"Regista con grado maggiore: {nodo_maggiore.name} (grado: {grado_maggiore})"))
        self._view._txt_result.controls.append(ft.Text(f"Regista con somma pesi incidendte massima: {nodo_massimo} (grado: {peso_massimo})"))


        self._view._txt_result.controls.append(ft.Text(f"\n"))

        self._view._txt_result.controls.append(ft.Text(f"Top 5 archi con peso maggiore:"))

        lista_ordinata_5 = self._model.cinque_archi_peso_maggiore()




        for i in range(0, len(lista_ordinata_5)):
            direttore1_nodo = lista_ordinata_5[i][0]
            direttore2_nodo = lista_ordinata_5[i][1]
            peso = lista_ordinata_5[i][2]["peso"]
            self._view._txt_result.controls.append(
                ft.Text(f"{i+1}. {direttore1_nodo.name} -- {direttore2_nodo.name} (peso: {peso})"))



        self._view.update_page()



    def handleTrovaGruppo(self, e):
        pass

