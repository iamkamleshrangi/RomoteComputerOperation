import yaml

with open('config.yaml', 'r') as f:
    doc = yaml.load(f)

def handler(tree,node):
    return doc[tree][node]
