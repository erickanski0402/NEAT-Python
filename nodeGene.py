class NodeGene:
    def __init__(self, type, id):
        self.type = type
        self.id = id
        pass

    def copy(self):
        return NodeGene(self.type, self.id)
