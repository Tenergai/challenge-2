consumptions = {
    "AC": 0.3299995377,
    "DishWasher": 0.6688335142,
    "WashingMachine": 0.4178148099,
    "Dryer": 1.170824143,
    "WaterHeater": 0.3608888889,
    "TV": 0.08422941935,
    "Microwave": 1.172379667,
    "Kettle": 1.99045825,
    "Lighting": 0.1362222223,
    "Refrigerator": 0.14,
}
# Device
#   Name, Consumption, Possible Hours, Hours On, Consecutive Hours

D1 = {
    "name": "AC",
    "consumption": 0.3299995377,
    "possibleHours":
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
    "hoursOn": 6,
    "consecutiveHours": 2
}
D2 = {
    "name": "DishWasher",
    "consumption": 0.6688335142,
    "possibleHours":
        [12, 13, 14, 19, 20, 21],
    "hoursOn": 2,
    "consecutiveHours": 1
}
D3 = {
    "name": "WashingMachine",
    "consumption": 0.4178148099,
    "possibleHours":
        [0, 1, 2, 3, 4, 5, 6, 15, 16, 17, 22, 23],
    "hoursOn": 2,
    "consecutiveHours": 2
}
D4 = {
    "name": "Dryer",
    "consumption": 1.170824143,
    "possibleHours":
        [0, 1, 2, 3, 4, 5, 6, 15, 16, 17, 22, 23],
    "hoursOn": 1,
    "consecutiveHours": 1
}
D5 = {
    "name": "WaterHeater",
    "consumption": 0.3608888889,
    "possibleHours":
        [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "hoursOn": 2,
    "consecutiveHours": 1
}
D6 = {
    "name": "TV",
    "consumption": 0.08422941935,
    "possibleHours":
        [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    "hoursOn": 3,
    "consecutiveHours": 1
}
D7 = {
    "name": "Microwave",
    "consumption": 1.172379667,
    "possibleHours":
        [7, 8, 12, 13, 19, 20],
    "hoursOn": 1.5,
    "consecutiveHours": 0.5
}
D8 = {
    "name": "Kettle",
    "consumption": 1.99045825,
    "possibleHours":
        [6, 7, 8, 12, 13, 17, 18, 19, 20, 22],
    "hoursOn": 0.25,
    "consecutiveHours": 0.25
}
D9 = {
    "name": "Lighting",
    "consumption": 0.1362222223,
    "possibleHours":
        [0, 1, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 22, 23],
    "hoursOn": 19,
    "consecutiveHours": 19
}
D10 = {
    "name": "Refrigerator",
    "consumption": 0.14,
    "possibleHours":
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
    "hoursOn": 24,
    "consecutiveHours": 24
}
# - 0 , 1 ,2 ,3 ,4 ,5 ,6 ,7 ,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23
# D1 AC - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
# D2 DishWasher - [12, 13, 14, 19, 20, 21]
# D3 WashingMachine - [0, 1, 2, 3, 4, 5, 6, 15, 16, 17, 22, 23]
# D4 Dryer - [0, 1, 2, 3, 4, 5, 6, 15, 16, 17, 22, 23]
# D5 WaterHeater - [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# D6 TV - [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
# D7 Microwave - [7, 8, 12, 13, 19, 20]
# D8 Kettle -  [6, 7, 8, 12, 13, 17, 18, 19, 20, 22]
# D9 Lighting - [0, 1, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 22, 23]
# D10 Refrigerator - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

# Microwave -> Dishwasher D7->D2
# WashingMachine -> Dryer D3 -> D4


precedences = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

]

print(precedences)


def getDevices():
    return [D1, D2, D3, D4, D5, D6, D7, D8, D9, D10]

def getPrecedences():
    return precedences


