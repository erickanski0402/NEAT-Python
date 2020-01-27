from random import randint, random, getrandbits
from connectionGene import ConnectionGene

class Genome:
    def __init__(self):
        self.connections = []
        self.nodes = []
        pass

    def addConnectionGene(self, newConnection):
        self.connections.append(newConnection)
        pass

    def addNodeGene(self, newNode):
        self.nodes.append(newNode)
        pass

    def addConnectionMutation(self):
        node_1 = self.nodes[randint(0, len(self.nodes))]
        node_2 = self.nodes[randint(0, len(self.nodes))]
        weight = ((random() * 2) - 1)
        reversed = False

        if ((node_1.type is "HIDDEN" and node_2.type is "INPUT")
        or (node_1.type is "OUTPUT" and node_2.type is "HIDDEN")
        or (node_1.type = "OUTPUT" and node_2.type is "INPUT")):
            reversed = True

        for conn in self.connections:
            if ((conn.inNode is node_1.id and conn.outNode is node_2.id)
            or (conn.inNode is node_2.id and conn.outNode is node_1.id)):
                return
            else:
                continue

        newConnection = ConnectionGene(node_1 if not reversed else node_2,
                                       node_2 if not reversed else node_1,
                                       weight,
                                       len(self.connections))
        self.addConnection(newConnection)
        pass

    def addNodeMutation(self):
        conn = self.connections[randint(0, len(self.connections))]

        inNode = conn.inNode
        outNode = conn.outNode

        conn.setExpression(False)

        newNode = NodeGene("HIDDEN", len(self.nodes))
        inToNew = ConnectionGene(inNode, newNode, 1, len(self.connections))
        newToOut = ConnectionGene(newNode, outNode, conn.weight, len(self.connections))

        self.addNode(newNode)
        self.addConnection(inToNew)
        self.addConnection(newToOut)
        pass

    def getConnectionByInnovationNumber(self, num):
        for conn in self.connections:
            if conn.innovationNumber is num:
                return conn
            else:
                continue
        return None

    def crossover(parent1, parent2):
        child = Genome()

        for node in parent1.nodes:
            child.addNodeGene(node.copy)

        for parent1Node in parent1.nodes:
            if parent2.getConnectionByInnovationNumber(parent1Node.innovationNumber) is not None: #Meaning they have matching genes
                childConnGene = parent1Node.copy() if bool(getrandbits(1)) else parent2.getConnectionByInnovationNumber(parent1Node.innovationNumber)
            else: #Non-matching genes
                childConnGene = parent1Node.copy()

            child.addConnectionGene(childConnGene)
            continue
        return child

# Write tests to verify functionality is good so far. Refer to example in paper provided
