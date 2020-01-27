from genome import Genome, crossover
from nodeGene import NodeGene
from connectionGene import ConnectionGene
from constants import INPUT, HIDDEN, OUTPUT
from helpers import printGenome

def testCrossover():
    parent1 = Genome()
    parent2 = Genome()

    parent1.addNodeGene(NodeGene(INPUT, 1))
    parent1.addNodeGene(NodeGene(INPUT, 2))
    parent1.addNodeGene(NodeGene(INPUT, 3))
    parent1.addNodeGene(NodeGene(HIDDEN, 5))
    parent1.addNodeGene(NodeGene(OUTPUT, 4))

    parent1.addConnectionGene(ConnectionGene(parent1.nodes.get(1), parent1.nodes.get(4), 2, 1))
    parent1.addConnectionGene(ConnectionGene(parent1.nodes.get(2), parent1.nodes.get(4), 2, 2))
    parent1.connections.get(2).setExpression(False)
    parent1.addConnectionGene(ConnectionGene(parent1.nodes.get(3), parent1.nodes.get(4), 2, 3))
    parent1.addConnectionGene(ConnectionGene(parent1.nodes.get(2), parent1.nodes.get(5), 2, 4))
    parent1.addConnectionGene(ConnectionGene(parent1.nodes.get(5), parent1.nodes.get(4), 2, 5))
    parent1.addConnectionGene(ConnectionGene(parent1.nodes.get(1), parent1.nodes.get(5), 2, 8))


    parent2.addNodeGene(NodeGene(INPUT, 1))
    parent2.addNodeGene(NodeGene(INPUT, 2))
    parent2.addNodeGene(NodeGene(INPUT, 3))
    parent2.addNodeGene(NodeGene(HIDDEN, 5))
    parent2.addNodeGene(NodeGene(HIDDEN, 6))
    parent2.addNodeGene(NodeGene(OUTPUT, 4))

    parent2.addConnectionGene(ConnectionGene(parent2.nodes.get(1), parent2.nodes.get(4), 2, 1))
    parent2.addConnectionGene(ConnectionGene(parent2.nodes.get(2), parent2.nodes.get(4), 2, 2))
    parent2.connections.get(2).setExpression(False)
    parent2.addConnectionGene(ConnectionGene(parent2.nodes.get(3), parent2.nodes.get(4), 2, 3))
    parent2.addConnectionGene(ConnectionGene(parent2.nodes.get(2), parent2.nodes.get(5), 2, 4))
    parent2.addConnectionGene(ConnectionGene(parent2.nodes.get(5), parent2.nodes.get(4), 2, 5))
    parent2.connections.get(5).setExpression(False)
    parent2.addConnectionGene(ConnectionGene(parent2.nodes.get(5), parent2.nodes.get(6), 2, 6))
    parent2.addConnectionGene(ConnectionGene(parent2.nodes.get(6), parent2.nodes.get(4), 2, 7))
    parent2.addConnectionGene(ConnectionGene(parent2.nodes.get(3), parent2.nodes.get(5), 2, 9))
    parent2.addConnectionGene(ConnectionGene(parent2.nodes.get(1), parent2.nodes.get(6), 2, 10))

    printGenome('Parent 1', parent1)
    printGenome('Parent 2', parent2)

    printGenome('Child', crossover(parent2, parent1))
    pass

testCrossover()
