'''
 * @Author: Bowei Hou 
 * @Date: 2020-02-21 20:52:34 
 * @Last Modified by:   Bowei Hou 
 * @Last Modified time: 2020-02-21 20:52:34 
'''


class Vertex(object):
    """Vertex of Graph.

    Each Vertex uses a dict to keep track of the vertices which connected.

    Attributes:
        id: the key value, str
        connectedTo: dict
    """

    def __init__(self, key):
        super().__init__()
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph(object):
    """Graph using Adjacency List.

    Attributes:
        vertList: vertices set
        numVertices: int
    """

    def __init__(self):
        super().__init__()
        self.verList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.verList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.verList:
            return self.verList[n]
        return None

    def __contains__(self, n):
        return n in self.verList

    def addEdge(self, f, t, cost=0):
        if f not in self.verList:
            nv = self.addVertex(f)

        if t not in self.verList:
            nv = self.addVertex(t)

        self.verList[f].addNeighbor(self.verList[t], cost)

    def getVertex(self):
        return self.verList.keys()

    def __iter__(self):
        return iter(self.verList.values())


g = Graph()
for i in range(6):
    g.addVertex(i)

g.addEdge(0, 1, 2)
for vertex in g:
    print(vertex)
    print(vertex.getConnections())
    print('\n')
