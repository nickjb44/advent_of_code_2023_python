import re
import sys

from src.day08.models.Node import Node
from src.day08.models.NodeLookup import NodeLookup

# I feel like this is a hack they probably didn't intend me
# to just work around...
# but I already wrote it recursively and I refuse to be
# bullied into making it iterative
sys.setrecursionlimit(100000)


def main(file_path):
    node_lookup: NodeLookup = NodeLookup()
    with open(file_path) as file:
        for line in file:
            line = line.rstrip()
            if 'R' in line and '=' not in line:
                direction_list = list(line)
            elif '=' in line:
                pattern = r'(\S+) = \((\S+), (\S+)\)'
                match = re.search(pattern, line)
                (node_name, left_name, right_name) = match.groups()
                node_lookup.add_node(node_name, left_name, right_name)

                # feels a bit silly to get what I just made but
                # returning the new node in add_node also feels weird
                node = node_lookup.get_node(node_name)

    start: Node = node_lookup.get_node("AAA")
    return start.seek_sleep(direction_list, 0, node_lookup)


if __name__ == "__main__":
    file_path = "input/input.txt"
    steps_to_sleep = main(file_path)

    print(f'it takes {steps_to_sleep} to sleep')
