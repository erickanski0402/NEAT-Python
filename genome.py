from random import randint, random, getrandbits
from connectionGene import ConnectionGene
from constants import INPUT, HIDDEN, OUTPUT

class Genome:
    def __init__(self):
        # Initializes genomes with empty dictionaries for connections/nodes
        self.connections = {}
        self.nodes = {}
        pass

    def addConnectionGene(self, newConnection):
        # Add new connection to dictionary with innovation number as key
        self.connections[newConnection.innovationNumber] = newConnection
        pass

    def addNodeGene(self, newNode):
        # Add new node to dictionary with id as key
        self.nodes[newNode.id] = newNode
        pass

    def addConnectionMutation(self):
        # Get two random nodes within the genome
        node_1 = self.nodes[randint(0, len(self.nodes))]
        node_2 = self.nodes[randint(0, len(self.nodes))]
        # Random weight between -1 and 1
        weight = ((random() * 2) - 1)
        reversed = False

        # Does the second node come before the first?
        if ((node_1.type is HIDDEN and node_2.type is INPUT)
        or (node_1.type is OUTPUT and node_2.type is HIDDEN)
        or (node_1.type is OUTPUT and node_2.type is INPUT)):
            # Ensures all connections are feed-forward
            reversed = True

        # Does this connection exist already?
        for conn in self.connections:
            if ((conn.inNode is node_1.id and conn.outNode is node_2.id)
            or (conn.inNode is node_2.id and conn.outNode is node_1.id)):
                # if yes, return out silently
                return
            else:
                # Otherwise continue
                continue

        newConnection = ConnectionGene(node_1 if not reversed else node_2,
                                       node_2 if not reversed else node_1,
                                       weight,
                                       len(self.connections))
        # Add new unique connection to genome
        self.addConnection(newConnection)
        pass

    def addNodeMutation(self):
        conn = self.connections[randint(0, len(self.connections))]

        inNode = conn.inNode
        outNode = conn.outNode

        conn.setExpression(False)

        newNode = NodeGene(HIDDEN, len(self.nodes))
        inToNew = ConnectionGene(inNode, newNode, 1, len(self.connections))
        newToOut = ConnectionGene(newNode, outNode, conn.weight, len(self.connections))

        self.addNode(newNode)
        self.addConnection(inToNew)
        self.addConnection(newToOut)
        pass

def crossover(parent1, parent2):
    child = Genome()

    for node in parent1.nodes.values():
        child.addNodeGene(node.copy())

    for parent1Node in parent1.connections.values():
        if parent2.connections.get(parent1Node.innovationNumber) is not None: #Meaning they have matching genes
            childConnGene = parent1Node.copy() if bool(getrandbits(1)) else parent2.connections.get(parent1Node.innovationNumber)
        else: #Non-matching genes
            childConnGene = parent1Node.copy()

        child.addConnectionGene(childConnGene)
        continue
    return child

# Write tests to verify functionality is good so far. Refer to example in paper provided
