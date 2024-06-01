import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self,e): #si attiva quando premo il bottone
        # estraggo distanza scelta
        distanza = self._view._txtIn.value
        # verifica che sia un numero float
        try:
            float(distanza)
        except:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Perfavore, inserisci un valore numerico"))
            self._view.update_page()
        # creo il grafo sul modello
        self._model.buildGraph(float(distanza))
        # pulisco la schermata
        self._view._txt_result.controls.clear()
        # inserisco i risultati
        self._view._txt_result.controls.append(ft.Text("Graph created!"))
        self._view._txt_result.controls.append(ft.Text("Num of nodes: " + str(self._model.numOfNodes())))
        self._view._txt_result.controls.append(ft.Text("Num of edges: " + str(self._model.numOfEdges())))
        allEdges = self._model.getAllEdges()
        for edge in allEdges:
            self._view._txt_result.controls.append(ft.Text(f"{edge[0]} <-> {edge[1]} ; DISTANZA MEDIA: {str(self._model.getPeso(edge[0],edge[1]))}"))
        # aggiorno
        self._view.update_page()


