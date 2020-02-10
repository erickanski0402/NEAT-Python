class InnovationTracker:
    def __init__(self):
        self.nextConnInnovationNumber = 1
        self.nextNodeInnvationNumber = 1
        self.connInnovations = {}
        pass

    def addConnInnovation(self, connString):
        self.connInnovations[connString] = self.nextConnInnovationNumber
        self.nextConnInnovationNumber += 1
        pass

    # Format of connString: '<inNode id>-><outNode id>'
    def resolveConnInnovationNumber(self, connString):
        if self.connInnovations.get(connString) is None:
            self.addConnInnovation(connString)

        return self.connInnovations.get(connString)

    def resolveNodeInnovationNumber(self):
        # Is this sufficient node tracking?
        nextNodeId = self.nextNodeInnvationNumber
        self.nextNodeInnvationNumber += 1
        return nextNodeId

    # Format of connString: '<inNode id>-><outNode id>'
    def doesConnectionExist(self, connString):
        return True if self.connInnovations.get(connString) is not None else False
