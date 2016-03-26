from random import randint

from historia.economy.enums import NaturalResource
from historia.world.biome import Biome

# Chance of each biome type to have a particular resource
resource_chances = {
    Biome.arctic: [
        (NaturalResource.iron, 10)
    ],
    Biome.tundra: [
        (NaturalResource.iron, 2)
    ],
    Biome.alpine_tundra: [
        (NaturalResource.iron, 2)
    ],
    Biome.desert: [
        (NaturalResource.iron, 2)
    ],
    Biome.shrubland: [
        (NaturalResource.iron, 1),
        (NaturalResource.trees, 1)
    ],
    Biome.savanna: [
        (NaturalResource.iron, 1)
    ],
    Biome.grasslands: [
        (NaturalResource.iron, 1),
        (NaturalResource.trees, 10)
    ],
    Biome.boreal_forest: [
        (NaturalResource.iron, 5),
        (NaturalResource.trees, 100)
    ],
    Biome.temperate_forest: [
        (NaturalResource.iron, 0.5),
        (NaturalResource.trees, 100)
    ],
    Biome.temperate_rainforest: [
        (NaturalResource.iron, 0.5),
        (NaturalResource.trees, 100)
    ],
    Biome.tropical_forest: [
        (NaturalResource.iron, 0.5),
        (NaturalResource.trees, 100)
    ],
    Biome.tropical_rainforest: [
        (NaturalResource.iron, 0.5),
        (NaturalResource.trees, 100)
    ]
}

# resources on coast
coast_resources = [
    (NaturalResource.fish, 10)
]

def chance_of_resource(chance):
    return randint(0, 100) <= chance

def give_hex_natural_resources(h):
    resources = resource_chances[h.biome]
    resources = [res for res, chance in resources if chance_of_resource(chance)]
    if h.is_coast:
        resources.extend([res for res, chance in coast_resources if chance_of_resource(chance)])

    h.natural_resources = resources
    return resources
