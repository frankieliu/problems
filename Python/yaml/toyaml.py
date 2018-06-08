import yaml
import pprint

d = {'A': 'a', 'B': {'C': 'c', 'D': 'd', 'E': 'e'}}

with open('result.yml', 'w') as yaml_file:
    yaml.dump(d, yaml_file, default_flow_style=False)

with open('result.yml', 'r') as yaml_file:
    e = yaml.load(yaml_file)

pp = pprint.PrettyPrinter(indent=4).pprint

pp(e)
