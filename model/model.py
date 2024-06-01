import networkx as nx
from networkx import Graph
from database.DAO import DAO


class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self._grafo = nx.Graph()
        self._IDMap = {}

    def buildGraph(self, distanza):
        # elimino eventuale grafo precedente
        self._grafo.clear()
        # mi servono i nodi del grafo = gli aeroporti -> prendo dal DAO
        self._nodes = DAO.getAllAirports()
        # creo mappa dei nodi -> IDMap[ID] = Aeroporto con quell'ID
        self.fillIDMap()
        # ora genero il grafo
        self._grafo.add_nodes_from(self._nodes)
        # adesso mi servono gli archi
        self._edges = DAO.getAllRotte()
        # per ogni arco verifico che sia rispettata la condizione

        for edge in self._edges:
            if float(edge.peso) >= distanza:
        # se è rispettata diventa un arco del grafo
                self._grafo.add_edge(edge.a1, edge.a2, weigth=float(edge.peso))


    def fillIDMap(self):
        for n in self._nodes:
            self._IDMap[n.ID] = n

    def numOfNodes(self):
        return self._grafo.number_of_nodes()

    def numOfEdges(self):
        return self._grafo.number_of_edges()

    def getAllEdges(self):
        return self._grafo.edges

    def getPeso(self, v1, v2):
        return self._grafo.get_edge_data(v1, v2)['weigth']