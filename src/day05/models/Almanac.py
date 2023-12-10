import re
from typing import Dict, Optional
from src.day05.models.Resource import Resource
from src.day05.models.Seed import Seed
from src.day05.utils.AlmanacLineParser import SeedLineStrategy, NewResourceMapStrategy, ClearResourcesStrategy, \
    AddResourceMappingStrategy, LineProcessingStrategy


class Almanac:

    def __init__(self):
        self.seeds: Seed = []
        # maps the string name to a resource
        self.resources: Dict[str, Resource] = {}
        # should be a better way to do this...
        self.current_resource_source: Optional[str] = None
        self.current_resource_destination: Optional[str] = None

    def from_almanac_file(self, almanac_file_path):
        with open(almanac_file_path) as almanac:
            for line in almanac:
                strategy: LineProcessingStrategy = self.determine_strategy(line.strip())
                strategy.process_line(line.rstrip(), self)

    def add_seed(self, seed: Seed):
        self.seeds.append(seed)

    def add_resource(self, name: str):
        if name in self.resources:
            # already there so don't bother updating
            return
        self.resources[name] = Resource(name)

    def determine_strategy(self, line):
        seed_line_pattern = r'^seeds:'
        new_resource_map_pattern = r".*?-to-.*? map:"
        clear_resources_pattern = r'^$'
        mapping_instructions_pattern = r'\d+ \d+ \d+'
        both_resources_set = self.current_resource_source and self.current_resource_destination

        if bool(re.search(seed_line_pattern, line)):
            return SeedLineStrategy()
        elif bool(re.search(new_resource_map_pattern, line)):
            return NewResourceMapStrategy()
        elif bool(re.search(clear_resources_pattern, line)):
            return ClearResourcesStrategy()
        elif bool(re.search(mapping_instructions_pattern, line)) and both_resources_set:
            return AddResourceMappingStrategy()
        else:
            raise NotImplementedError(f"Strategy not implemented for line found: {line}")

    def set_resources(self, source, destination):
        self.current_resource_source = source
        self.current_resource_destination = destination

    def clear_resources(self):
        self.current_resource_destination = None
        self.current_resource_destination = None

    def get_shortest_path_from_seed_to_location(self):
        if 'seed' not in self.resources:
            raise KeyError("cannot find seed, check initialization")
        seed_resource = self.resources['seed']

        return breadth_first_search_helper(seed_resource, "location")

def breadth_first_search_helper(start_resource:Resource, destination_name:str):
    current_resource = start_resource
    transform_sequence = []

    for next_resource in current_resource.resource_maps.keys():
        if next_resource.name == destination_name:
            tran
            return transform_sequence



