from random import random, getrandbits, choice
from connectionGene import ConnectionGene
from nodeGene import NodeGene
from constants import INPUT, HIDDEN, OUTPUT, WEIGHT_MUTATION_THRESHOLD
from helpers import generateNewWeight

class Genome:
    def __init__(self, innovationTracker):
        # Initializes genomes with empty dictionaries for connections/nodes
        self.connections = {}
        self.nodes = {}
        self.innovationTracker = innovationTracker
        pass

    def addConnectionGene(self, newConnection):
        # Add new connection to dictionary with innovation number as key
        self.connections[newConnection.innovationNumber] = newConnection
        pass

    def addNodeGene(self, newNode):
        # Add new node to dictionary with id as key
        self.nodes[newNode.id] = newNode
        pass

    def mutateWeights(self):
        # Selects a random connection from the genomes list of connectionGenes
        for conn in self.connections.values():
            if random() < WEIGHT_MUTATION_THRESHOLD:
                # 9 out of 10 times the connection is set with a new weight
                conn.setWeight(generateNewWeight())
            else:
                # 1 out of 10 times the connection weight is multiplied by a factor between -1 and 1
                conn.setWeight(conn.weight * 4 - 2)
        pass

    def addConnectionMutation(self):
        # Get two random nodes within the genome
        node_1 = choice(list(self.nodes.values()))
        node_2 = choice(list(self.nodes.values()))
        # Random weight between -1 and 1
        weight = generateNewWeight()
        reversed = False

        # Does the second node come before the first?
        if ((node_1.type is HIDDEN and node_2.type is INPUT)
        or (node_1.type is OUTPUT and node_2.type is HIDDEN)
        or (node_1.type is OUTPUT and node_2.type is INPUT)):
            # Ensures all connections are feed-forward
            reversed = True

        # connString format <Input node id>-><Output node id>
        connString = f'{node_1.id}->{node_2.id}' if not reversed else f'{node_2.id}->{node_1.id}'

        # Does this connection exist already?
        if ((self.innovationTracker.doesConnectionExist(connString))
        # Or is the node recurrent? (unclear if this is an issue)
        or (node_1.id is node_2.id)):
            # if so, return silently
            return

        newConnection = ConnectionGene(node_1 if not reversed else node_2,
                                       node_2 if not reversed else node_1,
                                       weight,
                                       self.innovationTracker.resolveConnInnovationNumber(connString))
        # Add new unique connection to genome
        self.addConnectionGene(newConnection)
        pass

    def addNodeMutation(self):
        # Selects random connection
        conn = choice(list(self.connections.values()))

        inNode = conn.inNode
        outNode = conn.outNode

        # Disables old connection
        conn.setExpression(False)

        # Creates new node at center of split
        newNode = NodeGene(HIDDEN, self.innovationTracker.resolveNodeInnovationNumber())
        # creates a new connection for inNode->newNode
        inToNew = ConnectionGene(inNode, newNode, 1, self.innovationTracker.resolveConnInnovationNumber(f'{inNode.id}->{newNode.id}'))
        # creates a new connection for newNode->outNode
        newToOut = ConnectionGene(newNode, outNode, conn.weight, self.innovationTracker.resolveConnInnovationNumber(f'{newNode.id}->{outNode.id}'))

        # Add new node and connections to genome
        self.addNodeGene(newNode)
        self.addConnectionGene(inToNew)
        self.addConnectionGene(newToOut)
        pass

    def crossover(parent1, parent2):
        # Parent 1 is assumed to have the higher fitness
        child = Genome(parent1.innovationTracker)

        # Copies all nodes from the most fit parent
        for node in parent1.nodes.values():
            child.addNodeGene(node.copy())

        # Begins cross pollinating connections between both parents
        for parent1Node in parent1.connections.values():
            if parent2.connections.get(parent1Node.innovationNumber) is not None: # Meaning they have matching genes
                # When parents have matching connection genes, randomly select which connection to copy to child
                childConnGene = parent1Node.copy() if bool(getrandbits(1)) else parent2.connections.get(parent1Node.innovationNumber)
            else: # Non-matching genes
                # Defaults to more fit parent when connection genes dont match
                childConnGene = parent1Node.copy()

            child.addConnectionGene(childConnGene)
            continue
        return child

# Write tests to verify functionality is good so far. Refer to example in paper provided
