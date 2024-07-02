import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.maxLen = None
        self.solBest = None
        self.grafo=nx.Graph()
        self.idMap={}

    def getRuoli(self):
        return DAO.getRuoliDAO()

    def creaGrafo(self,ruolo):
        self.grafo.clear()
        nodi=DAO.getNodi(ruolo)
        self.grafo.add_nodes_from(nodi)
        for a in nodi:
            self.idMap[a.artist_id]=a

        archi=DAO.getArchi(ruolo)
        for a in archi:
            self.grafo.add_edge(self.idMap[a[0]],self.idMap[a[1]],peso=a[2])
        pass

    def getDetails(self):
        return len(self.grafo.nodes), len(self.grafo.edges)


    def getConnessi(self):
        res= list(self.grafo.edges(data=True))
        resSort = sorted(res,key=lambda x: x[2]["peso"])
        return resSort

    def controllaId(self,id):
        if id in self.idMap.keys():
            return True
        else:
            return False

    def cammino(self,id):
        self.solBest=[]
        self.maxLen=0
        self.ricorsione([self.idMap[id]],self.idMap[id])
        print(self.maxLen,self.solBest)

        pass

    def ricorsione(self, parziale, start):

        succ=list(self.grafo.neighbors(start))
        ammissibili= self.getAmmissibili(parziale,succ)

        if self.isTerminale(parziale,ammissibili):
            if len(parziale)> self.maxLen:
                self.maxLen=len(parziale)
                self.solBest=copy.deepcopy(parziale)
        else:
            for a in ammissibili:
                parziale.append(a)
                self.ricorsione(parziale,a)
                parziale.pop()

        pass

    def getAmmissibili(self, parziale, succ):
        if len(parziale)<2:
            return succ

        ammissibili=[]
        start=parziale[-1]
        for a in succ:
            if a not in parziale:
                if self.grafo[start][a]["peso"]== self.grafo[parziale[-2]][start]["peso"]:
                    ammissibili.append(a)
        return ammissibili
        pass

    def isTerminale(self, parziale, ammissibili):
        if len(ammissibili)==0:
            return True
        return False
        pass
