class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

    def __repr__(self):
        done = {}
        return self.help_repr(self, done)

    def help_repr(self, node, done):
        out = []
        if node.label not in done:
            out.append(node.label + " -> " + str([x.label for x in node.neighbors]))
            done[node.label] = True
            # print(done)
            for x in self.neighbors:
                out.append(self.help_repr(x, done))
        return " ".join(out)
