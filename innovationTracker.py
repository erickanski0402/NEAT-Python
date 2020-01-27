class InnovationTracker:
    def __init__(self):
        self.nextInnovationNumber = 1
        self.innovations = {}
        pass

    def addInnovation(self, connString):
        self.innovations[connString] = self.nextInnovationNumber
        self.nextInnovationNumber += 1
        pass

    # Format of connString: 'inNode id->outNode id'
    def resolveInnovationNumber(self, connString):
        if innovations.get(connString) is None:
            self.addInnovation(connString)
            
        return self.innovations.get(connString)
