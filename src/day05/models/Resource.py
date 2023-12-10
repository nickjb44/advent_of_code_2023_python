from typing import Dict


class Resource:
    def __init__(self, name):
        self.name = name
        self.resource_maps: Dict[Resource, CoordinateMapper] = {}

    def add_resource_to_map(self, destination_resource):
        if destination_resource in destination_resource:
            # checking that we're not overwriting anything
            raise KeyError(f"overwriting an existing resource {destination_resource} in {self} shouldn't be allowed")
        self.resource_maps[destination_resource] = CoordinateMapper()

    def update_map(self, source_start, destination_start, n_to_map, destination_resource):
        coordinate_mapper = self.resource_maps[destination_resource]
        for i in range(n_to_map):
            # this should parse the line and make
            source_index = source_start + i
            destination_index = destination_start + i
            if source_index in coordinate_mapper.source_to_destination:
                raise KeyError(f"source index for {destination_index} in {self} shouldn't be set twice")
            coordinate_mapper.source_to_destination[source_index] = destination_index

    def source_value_to_destination_value(self, source_value, destination_resource):
        if destination_resource not in self.resource_maps:
            # consider raising error instead
            print(f'might be an error {destination_resource} not found in {self}, direct mapping not possible')
            return None





    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if not isinstance(other, Resource):
            raise NotImplementedError(f"not implemented for {type(other)}")
        self.name == other.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class CoordinateMapper:
    def __init__(self):
        self.source_to_destination: Dict[int, int] = {}

    def get_destination_value(self, source_value):
        if source_value in self.source_to_destination:
            return self.source_to_destination[source_value]
        return source_value
