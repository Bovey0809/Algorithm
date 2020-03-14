'''
 * @Author: Bowei Hou 
 * @Date: 2020-02-21 20:52:34 
 * @Last Modified by:   Bowei Hou 
 * @Last Modified time: 2020-02-21 20:52:34 
'''


from functools import reduce


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
        self.visited = False

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self) -> list:
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

    def addEdgeList(self, f, t: list, cost=0):
        for node in t:
            self.addEdge(f, node)

    def getVertices(self):
        return self.verList.keys()

    def __iter__(self):
        return iter(self.verList.values())

    def __getitem__(self, i):
        return self.getVertex(i)
# create a Graph

test_g = Graph()
for i in range(1, 7):
    test_g.addVertex(i)

test_g.addEdgeList(1, [2, 3, 4])
test_g.addEdgeList(2, [1, 5])
test_g.addEdge(3, 4)
test_g.addEdgeList(4, [1, 3, 5, 6])
test_g.addEdgeList(5, [2, 4, 5])
test_g.addEdgeList(6, [4, 5])

# Deep first traversal
# iteration version


def depthFirstTraverse(node: Vertex):
    # iterative
    stack = [node]
    while stack:
        node = stack.pop()
        for link in node.getConnections():
            if not link.visited:
                print(link)
                link.visited = True
                stack.append(link)
depthFirstTraverse(test_g.getVertex(1))
