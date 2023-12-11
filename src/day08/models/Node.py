
class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def seek_sleep(self, direction_list, steps_taken, node_lookup):
        if self.is_sleep():
            return steps_taken
        direction = direction_list[steps_taken % len(direction_list)]
        steps_taken += 1
        if direction == "L":
            next_node_name = self.left
        elif direction == "R":
            next_node_name = self.right
        else:
            # would be cleaner to do an enum, maybe refactor later
            raise ValueError(f" direction {direction} is not valid")

        next_node = node_lookup.get_node(next_node_name)

        return next_node.seek_sleep(direction_list, steps_taken, node_lookup)

    def find_sleep_cycle_distance(self, direction_list, node_lookup):
        current_node = self
        steps_taken = 0

        while not current_node.is_rest():
            direction = direction_list[steps_taken % len(direction_list)]
            current_node = current_node.follow_direction(direction, node_lookup)
            steps_taken += 1
        first_found = current_node
        first_found_at = steps_taken

        # now do it until you find that node again
        direction = direction_list[steps_taken % len(direction_list)]
        current_node = current_node.follow_direction(direction, node_lookup)
        steps_taken += 1

        while not current_node.name == first_found.name:
            direction = direction_list[steps_taken % len(direction_list)]
            current_node = current_node.follow_direction(direction, node_lookup)
            steps_taken += 1

        return (
             first_found_at,
             steps_taken - first_found_at
        )

    def follow_direction(self, direction, node_lookup):
        if direction == "L":
            return node_lookup.get_node(self.left)
        elif direction == "R":
            return node_lookup.get_node(self.right)
        else:
            raise ValueError(f"Cannot recognize direction {direction}")

    def is_sleep(self):
        return self.name == "ZZZ"

    def is_rest(self):
        return self.name[-1] == "Z"
