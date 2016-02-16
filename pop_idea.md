# Pops
Pops are units of population on the county (hex, or lowest political division) level.

## Pop properties
- size: how many people are represented by this pop
- culture
- religion
- job
- militancy: chance of revolting
- productivity
- money

## Needs
Pops need money in order to survive. Every day they purchase and consume goods. If a Pop is meeting all its needs, it saves up money.

### Types of Needs
- Basic Needs: needed to survive. A pop only meeting basic needs will not advance. If a pop is not meeting its basic needs, its size will decrease (death).
- Daily Needs: needed for happiness. A pop not meeting these needs will be unhappy and might migrate. A pop meeting these needs might promote and/or grow.
- Luxury Needs: needed for to save up money. A pop that is meeting its luxury needs is happy and less militant. It will grow very fast.


## Happiness
Happiness is a measure of (in order of decreasing importance):
- employment
- safety (if a war is going on, pillage and rape, etc)
- freedom (to practice religion, express culture)

## Growth
If a pop is happy, it will grow in size.

## Migration
If a pop is unhappy, it will leave the county. It will look for other counties to migrate to, even if they're not in the same country. If no migration target can be found, they stay in the county but their size decreases anyway (meaning they're dying). In this case, their militancy increases rapidly.

## Death
If the size of the pop reaches 0, it will be deleted.

## Types
Each pop has a type, representing their primary role in society (usually their employment).

### List of Pop types
- Soldier: employed as a member of the military. Called upon in times of war to fight.
- Officer: trained leader in the military. Will make the military more productive
- Slaves: works in Mines and Farms at a reduced efficiency
- Laborer: works in Mines
- Farmer: works in Farms
- Rancher: works in ranches
- Clergy: increase literacy. Members of the state religion. Provide some research points
- Scholars: greatly increase literacy, provide research points
- Educators: increase literacy in the pop they exist in
- Aristocrats: aristocracy and nobles
- Craftsman: produce goods in a workshop
- Merchants: sell and redistribute goods

- Fisherman: works in nature (coastal hexes only)
- Hunter: works in nature
- Herder: works in nature
- Gatherer: works in nature

## Promotion and Demotion
A pop can promote or demote to another type if certain criteria are met.

Slave -> Farmer or Laborer (if freed)
Laborer -> Craftsman
Craftsman -> Merchant
Laborer -> Educator
Educator -> Scholar
Farmer, Rancher <-> Rancher, Farmer
Hunter, Gatherer <-> Hunter, Gatherer
Hunter, Gatherer -> Herder
Herder -> Laborer
Hunter, Gatherer -> Laborer
Craftsman -> Merchant
Aristocrats <-> Merchant
Farmer, Laborer, Craftsman -> Soldier
Soldier <-> Officer
Slave <- (Any)

### Promotion Criteria
- pop is meeting its basic and daily needs
- can promote to a higher type
- demand exists for pops of that higher type

## Pop Creation
When a new pop is promoted, a certain number of them will move to a new pop with the same properties but with the new type.

e.g. Pop 1: 1000 Irish Catholic Farmers (8 promoting to Craftsman per month)
            net: -8 (change in employment)
     Pop 2     8 Irish Catholic Craftsman (net: +8)
            net: +8 (change in employment)

e.g. Pop 1: 500 Ukrainian Orthodox Farmers (not meeting basic needs)
            net: -122 (starvation)

In the first example, if a new pop is required due to a change in size in another pop, it will be created.
In the second example, no new pop was created because of death.




# Goods and Production
Goods are produced in production centers where they are worked by pops.

## Production Centers

### Buildings (must be built)
Mines: employ laborers and produces some raw materials
       requires Iron, Copper, Gold, Tin resources on hex
Farms: employ Farmers and produces some raw materials
Ranch: employs Ranchers and produces Cattle, Milk
Workshops: employ Craftsmen produces Manufactured Goods. Can produce multiple things

### Natural (exist in nature)
Fishery: employs Farmers
Herds: employs Farmers and produces Cattle, Milk
Forest: employs Laborers (gathering)

Each may employ a fixed number of pops of a certain type.


## Types of goods

### Raw Materials

| name         | producer  | biome      |
| ------------ | --------- | ---------- |
| gold         | Mine      | all        |             
| silver       | Mine      | all        |        
| iron         | Mine      | all        |        
| copper       | Mine      | all        |        
| wheat        | Field     | grassland  |             
| rye          | Field     | all        |             
| corn         | Field     | all        |             
| rice         | Field     | all        |             
| berries      | Field     | all        |             
| cattle       | Farm      | all        |        
| pig          | Farm      | all        |        
| chicken      | Farm      | all        |        
| flax         | Field     | all        |             
| cotton       | Field     | all        |             
| hemp         | Field     | all        |             
| milk         | Farm      | all        |        
| fish         | Fishery   | all        |             
| wood         | n/a       | all        |        
| dye          |           | all        |        
| spices       | Field     | all        |             
| coffee       |           | all        |   
| fruit        |           | all        |   
| vegetables   |           | all        |   
| tea          |           | all        |   
| wine         |           | all        |   
| beer         |           | all        |   
| silk         |           | all        |   
| tobacco      |           | all        |   

### Manufactured Goods
Requirements in parenthesis

#### First-level
- Swords (iron)
- Bows (wood and iron)
- Trebuchets (wood and iron)
- linen (cotton or hemp or flax)

#### Second-level
- clothes (linen)
- fine clothes (linen, dye)
- uniforms (linen, wool, dye)




# Technology
Technology allows various jobs

- Agriculture allows plant farming
- Aquaculture allows intensive fish farming
- Animal Husbandry allows animal farming
    - domesticated cattle (meat)
    - domesticated pig (meat)
    - domesticated sheep (wool)


# Technical
## Simulation Start

For a few hexes on the map:
    Generate a few tribes at these hexes.
    For each tribe:
        Generate pops such that:
            70% are Farmers
            10% are Aristocrats
            5% are Clergy
            5% are Soldiers
        Generate Production Centers to employ the above pops

## Simulation Loop
- for all countries:
     - for all second-level divisions:
          - for all pops
               - if not main religion:
                    - check religions conversion
               - if not main culture:
                    - check culture conversion
               - calculate chance in:
                    - happiness
                    - militancy
                    - literacy
               - buy as much needs as current saved money
               - calculate promotion and demotion
               - calculate population change due to the above, which pop to move to or create
               - delete if size is 0
