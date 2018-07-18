import yaml
import pickle
import re


class add2():

    def __init__(self):
        self.name = type(self).__name__
        operands = [int(s) for s in re.findall(r'\d+', self.name)]
        self.operand = operands[0]

    def do(self):
        with open('store/store.yml', 'r') as yaml_file:
            self.y = yaml.load(yaml_file)
        self.dports = self.y[self.name]
        self.inn = pickle.load(
            open(self.dports['in'], "rb"))
        self.out = self.inn + self.operand
        pickle.dump(self.out, open(self.dports['out'], "wb"))

    def desc(self):
        return self.name
