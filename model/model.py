import networkx as nx
from database.DAO import DAO


class Model:

    def __init__(self):
        self.contiguities = None
        self.countries = None
        self.grafo = nx.Graph()
        self._idMap = {}

    def getCountries(self):
        return DAO.getCountries()


    def buildGrafo(self, year):
        self.contiguities = DAO.get_contiguity_year(year)
        self.countries = DAO.get_all_countries(year)
        for c in self.countries:
            self._idMap[c.CCode] = c
        self.grafo.add_nodes_from(self.countries)
        #self.grafo.clear()
        for c in self.contiguities:
            u = self._idMap[c.state1no]
            v = self._idMap[c.state2no]
            self.grafo.add_edge(u, v)

        print(self.grafo)

    def get_num_compConn(self):
        connComp = nx.connected_components(self.grafo)
        return (connComp)

    #MODO 1) RICERCA DEGLI STATI RAGGIUNGIBILI ATTRAVERSO IL METODO BFS
    def getBFSNodes(self, source):
        edges = nx.bfs_edges(self.grafo, source)
        visited = []
        for u, v in edges:
            visited.append(v)
        return visited

    # MODO 2) RICERCA DEGLI STATI RAGGIUNGIBILI ATTRAVERSO IL METODO DFS
    def getDFSNodes(self, source):
        edges = nx.dfs_edges(self.grafo, source)
        visited = []
        for u, v in edges:
            visited.append(v)
        return visited

    # MODO 3) RICORSIONE ??? rivedi
    def find_reachable_states(self, stato, visitato):
        visitato = []

        for neighbor in self.grafo[stato]:
            if neighbor not in visitato:
                visitato.add(stato)
                self.find_reachable_states(neighbor, visitato)
        return visitato

    def vicini(self, stato):
        for stato in self.grafo.nodes:
            num_confinanti = len(list(self.grafo.neighbors(stato)))
            print(f"{stato}: {num_confinanti} stati confinanti")









