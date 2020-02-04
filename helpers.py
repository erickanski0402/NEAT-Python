from random import random

def printConnections(connections):
    for conn in connections.values():
        printConnection(conn)
    pass

def printNodes(nodes):
    for node in nodes.values():
        printNode(node)
    pass

def printConnection(connection):
    print(f'INNOVATION: {connection.innovationNumber}, {connection.inNode.id} -> {connection.outNode.id}, EXPRESSED: {connection.expressed}, WEIGHT: {connection.weight}')
    pass

def printNode(node):
    print(f'[ID: {node.id}, TYPE: {node.type}]')
    pass

def printGenome(name, genome):
    print(f'--------------------------{name}----------------------------')
    printNodes(genome.nodes)
    printConnections(genome.connections)
    print('--------------------------------------------------------------')
    pass

def generateNewWeight():
    return random() * 2 - 1
