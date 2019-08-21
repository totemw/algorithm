class Monarch(object):
    def __init__(self):
        self.name = None
        self.childern = []
        self.isAlive = True


class Monarchy(object):
    def __init__(self):
        self.firstMonarch = None
        self.monarchs = {}

    def birth(self, child, parent):
        # create monarch
        monarch = Monarch()
        monarch.name = child
        # If it's the first monarch
        if (parent == None and self.firstMonarch == None):
            self.firstMonarch = monarch
        else:
            # find parent and add child
            if not (parent in self.monarchs):
                return
            self.monarchs[parent].childern.append(monarch)
        # Add the monarch to hash table
        self.monarchs[child] = monarch

    def death(self, name):
        self.monarchs[name].isAlive = False

    def preOrder(self, node):
        if (node):
            if (node.isAlive == True):
            # don't print dead people :'(
                print("alive")
            for child in node.childern:
                self.preOrder(child)

    def getOrderOfSuccession(self):
        self.preOrder(self.firstMonarch)

