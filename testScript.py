from genome import Genome
from nodeGene import NodeGene
from connectionGene import ConnectionGene
from innovationTracker import InnovationTracker
from constants import INPUT, HIDDEN, OUTPUT
from helpers import printGenome
from random import random

def testCrossover():
    print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>TEST CROSSOVER<<<<<<<<<<<<<<<<<<<<<<<<<')
    # Global innovation number tracking object
    inTracker = InnovationTracker()
    parent1 = Genome(inTracker)
    parent2 = Genome(inTracker)

    parent1.addNodeGene(NodeGene(INPUT, 1))
    parent1.addNodeGene(NodeGene(INPUT, 2))
    parent1.addNodeGene(NodeGene(INPUT, 3))
    parent1.addNodeGene(NodeGene(HIDDEN, 5))
    parent1.addNodeGene(NodeGene(OUTPUT, 4))

    parent1.addConnectionGene(ConnectionGene(parent1.nodes.get(1), parent1.nodes.get(4), ((random() * 2) - 1), 1))
    parent1.addConnectionGene(ConnectionGene(parent1.nodes.get(2), parent1.nodes.get(4), ((random() * 2) - 1), 2))
    parent1.connections.get(2).setExpression(False)
    parent1.addConnectionGene(ConnectionGene(parent1.nodes.get(3), parent1.nodes.get(4), ((random() * 2) - 1), 3))
    parent1.addConnectionGene(ConnectionGene(parent1.nodes.get(2), parent1.nodes.get(5), ((random() * 2) - 1), 4))
    parent1.addConnectionGene(ConnectionGene(parent1.nodes.get(5), parent1.nodes.get(4), ((random() * 2) - 1), 5))
    parent1.addConnectionGene(ConnectionGene(parent1.nodes.get(1), parent1.nodes.get(5), ((random() * 2) - 1), 8))


    parent2.addNodeGene(NodeGene(INPUT, 1))
    parent2.addNodeGene(NodeGene(INPUT, 2))
    parent2.addNodeGene(NodeGene(INPUT, 3))
    parent2.addNodeGene(NodeGene(HIDDEN, 5))
    parent2.addNodeGene(NodeGene(HIDDEN, 6))
    parent2.addNodeGene(NodeGene(OUTPUT, 4))

    parent2.addConnectionGene(ConnectionGene(parent2.nodes.get(1), parent2.nodes.get(4), ((random() * 2) - 1), 1))
    parent2.addConnectionGene(ConnectionGene(parent2.nodes.get(2), parent2.nodes.get(4), ((random() * 2) - 1), 2))
    parent2.connections.get(2).setExpression(False)
    parent2.addConnectionGene(ConnectionGene(parent2.nodes.get(3), parent2.nodes.get(4), ((random() * 2) - 1), 3))
    parent2.addConnectionGene(ConnectionGene(parent2.nodes.get(2), parent2.nodes.get(5), ((random() * 2) - 1), 4))
    parent2.addConnectionGene(ConnectionGene(parent2.nodes.get(5), parent2.nodes.get(4), ((random() * 2) - 1), 5))
    parent2.connections.get(5).setExpression(False)
    parent2.addConnectionGene(ConnectionGene(parent2.nodes.get(5), parent2.nodes.get(6), ((random() * 2) - 1), 6))
    parent2.addConnectionGene(ConnectionGene(parent2.nodes.get(6), parent2.nodes.get(4), ((random() * 2) - 1), 7))
    parent2.addConnectionGene(ConnectionGene(parent2.nodes.get(3), parent2.nodes.get(5), ((random() * 2) - 1), 9))
    parent2.addConnectionGene(ConnectionGene(parent2.nodes.get(1), parent2.nodes.get(6), ((random() * 2) - 1), 10))

    printGenome('Parent 1', parent1)
    printGenome('Parent 2', parent2)

    printGenome('Child', Genome.crossover(parent2, parent1))
    pass

def testAddConnectionMutation():
    print('\n>>>>>>>>>>>>>>>>>>>TEST ADD CONNECTION MUTATION<<<<<<<<<<<<<<<<<<<<')
    inTracker = InnovationTracker()
    gen = Genome(inTracker)

    node1 = NodeGene(INPUT, gen.innovationTracker.resolveNodeInnovationNumber())
    node2 = NodeGene(OUTPUT, gen.innovationTracker.resolveNodeInnovationNumber())

    gen.addNodeGene(node1)
    gen.addNodeGene(node2)

    printGenome('Gen Before', gen)
    gen.addConnectionMutation()
    printGenome('Gen After', gen)
    pass

def testAddNodeMutation():
    print('\n>>>>>>>>>>>>>>>>>>>>>>TEST ADD NODE MUTATION<<<<<<<<<<<<<<<<<<<<<<')
    inTracker = InnovationTracker()
    gen = Genome(inTracker)

    node1 = NodeGene(INPUT, gen.innovationTracker.resolveNodeInnovationNumber())
    node2 = NodeGene(OUTPUT, gen.innovationTracker.resolveNodeInnovationNumber())

    gen.addNodeGene(node1)
    gen.addNodeGene(node2)

    gen.addConnectionMutation()
    printGenome('Gen Before', gen)

    gen.addNodeMutation()
    printGenome('Gen After', gen)
    pass

testCrossover()
testAddConnectionMutation()
testAddNodeMutation()
