import re
from abc import ABC, abstractmethod

from src.day05.models.Resource import Resource
from src.day05.models.Seed import Seed


class LineProcessingStrategy(ABC):
    @abstractmethod
    def process_line(self, line, almanac):
        pass


class SeedLineStrategy(LineProcessingStrategy):
    def process_line(self, line, almanac):
        # line looks like following
        # seeds: 10 23 45
        seed_ids = line.split(":")[1].split()

        for seed_id in seed_ids:
            try:
                seed_id = int(seed_id)
            except ValueError:
                raise ValueError(f"seed {seed_id} doesn't look like an integer")
            seed = Seed(seed_id)
            almanac.add_seed(seed)

        return


class NewResourceMapStrategy(LineProcessingStrategy):
    def process_line(self, line, almanac):
        resource_extraction_pattern = r"(\w+)-to-(\w+) map:"
        resources_match = re.search(resource_extraction_pattern, line)
        if not resources_match:
            raise ValueError(f"could not parse line {line} into resources")
        (source, destination) = (resources_match.group(1), resources_match.group(2))
        almanac.add_resource(source)
        almanac.current_resource_source = source
        almanac.add_resource(destination)
        almanac.current_resource_destination = destination

        source_resource: Resource = almanac.resources[source]
        source_resource.add_resource_to_map(Resource)

        destination_resource: Resource = almanac.resources[destination]
        destination_resource.add_resource_to_map(Resource)
        return


class ClearResourcesStrategy(LineProcessingStrategy):
    def process_line(self, line, almanac):
        almanac.current_resource_source = None
        almanac.current_resource_destination = None
        return


class AddResourceMappingStrategy(LineProcessingStrategy):
    def process_line(self, line, almanac):
        source_resource_name = almanac.current_resource_source
        destination_resource_name = almanac.current_resource_destination

        source_resource: Resource = almanac.resources[source_resource_name]
        destination_resource: Resource = almanac.resources[destination_resource_name]

        source_destination_range_pattern = r'(\d+) (\d+) (\d+)'
        match = re.search(source_destination_range_pattern, line)
        (source_start, destination_start, n_to_map) = (match.group(1), match.group(2), match.group(3))
        source_start = int(source_start)
        destination_start = int(destination_start)
        n_to_map = int(n_to_map)

        source_resource.update_map(
            source_start=source_start,
            destination_start=destination_start,
            n_to_map=n_to_map,
            destination_resource=destination_resource
        )

        destination_resource.update_map(
            source_start=destination_start,
            destination_start=source_start,
            n_to_map=n_to_map,
            destination_resource=source_resource
        )
        return
