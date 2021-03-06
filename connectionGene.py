class ConnectionGene:
    def __init__(self, inNode, outNode, weight, innovationNumber):
        self.inNode = inNode
        self.outNode = outNode
        self.weight = weight
        self.expressed = True
        self.innovationNumber = innovationNumber
        pass

    def setExpression(self, flag):
        self.expressed = flag
        pass

    def setWeight(self, weight):
        self.weight = weight
        pass

    def copy(self):
        return ConnectionGene(self.inNode,
                              self.outNode,
                              self.weight,
                              self.innovationNumber)
