from historia.economy.enums import Resource

# Chance of each biome type to have a particular resource
resource_chances = {
    Biome.arctic: [
        (Resource.iron, 10)
    ],
    Biome.tundra: [
        (Resource.iron, 2)
    ],
    Biome.alpine_tundra: [

    ],
    Biome.desert: [

    ],
    Biome.shrubland: [

    ],
    Biome.savanna: [

    ],
    Biome.grasslands: [

    ],
    Biome.boreal_forest: [

    ],
    Biome.temperate_forest: [

    ],
    Biome.temperate_rainforest: [

    ],
    Biome.tropical_forest: [

    ],
    Biome.tropical_rainforest: [

    ]
}

# hexes around rivers are more likely to have these resources
river_modifiers = {

}

def give_hex_natural_resources(hex):
