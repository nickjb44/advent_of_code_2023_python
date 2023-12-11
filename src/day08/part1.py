import re
from typing import List

from src.day08.models.Node import Node
from src.day08.models.NodeLookup import NodeLookup
from sympy.ntheory.modular import solve_congruence


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

    ghost_starts = [node_lookup.get_node(node_name) for node_name in node_lookup.start_nodes]
    return seek_eternal_rest(ghost_starts, node_lookup, direction_list)[1]


def seek_eternal_rest(ghost_positions: List[Node], node_lookup, direction_list):
    ghost_cycle_offset_and_cycle_length = [
        ghost_position.find_sleep_cycle_distance(direction_list, node_lookup)
        for ghost_position in ghost_positions
    ]
    return solve_congruence(*ghost_cycle_offset_and_cycle_length)


if __name__ == "__main__":
    file_path = "input/input.txt"
    steps_to_sleep = main(file_path)
    print(f'it takes {steps_to_sleep} steps for all ghosts to find rest')
