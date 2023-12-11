from src.day08.models.Node import Node


class NodeLookup:
    def __init__(self):
        self.nodes = {}
        self.start_nodes = []
        self.end_nodes = []

    def add_node(self, node_name, left_name, right_name):
        if node_name in self.nodes:
            return
        self.nodes[node_name] = Node(node_name, left_name, right_name)
        if node_name[-1] == "A":
            self.start_nodes.append(node_name)
        if node_name[-1] == "Z":
            self.end_nodes.append(node_name)

    def get_node(self, node_name):
        if node_name not in self.nodes:
            raise KeyError(f'could not find node {node_name}')
        return self.nodes[node_name]
