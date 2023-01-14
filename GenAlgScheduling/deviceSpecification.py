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

D0 = {
    "name": "AC",
    "consumption": 0.3299995377,
    "possibleHours":
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
    "hoursOn": 6,
    "consecutiveHours": 2
}
D1 = {
    "name": "DishWasher",
    "consumption": 0.6688335142,
    "possibleHours":
        [12, 13, 14, 19, 20, 21],
    "hoursOn": 2,
    "consecutiveHours": 1
}
D2 = {
    "name": "WashingMachine",
    "consumption": 0.4178148099,
    "possibleHours":
        [0, 1, 2, 3, 4, 5, 6, 15, 16, 17, 22, 23],
    "hoursOn": 2,
    "consecutiveHours": 2
}
D3 = {
    "name": "Dryer",
    "consumption": 1.170824143,
    "possibleHours":
        [0, 1, 2, 3, 4, 5, 6, 15, 16, 17, 22, 23],
    "hoursOn": 1,
    "consecutiveHours": 1
}
D4 = {
    "name": "WaterHeater",
    "consumption": 0.3608888889,
    "possibleHours":
        [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "hoursOn": 2,
    "consecutiveHours": 1
}
D5 = {
    "name": "TV",
    "consumption": 0.08422941935,
    "possibleHours":
        [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    "hoursOn": 3,
    "consecutiveHours": 1
}
D6 = {
    "name": "Microwave",
    "consumption": 1.172379667,
    "possibleHours":
        [7, 8, 12, 13, 19, 20],
    "hoursOn": 1,
    "consecutiveHours": 1
}
D7 = {
    "name": "Kettle",
    "consumption": 1.99045825,
    "possibleHours":
        [6, 7, 8, 12, 13, 17, 18, 19, 20, 22],
    "hoursOn": 1,
    "consecutiveHours": 1
}
D8 = {
    "name": "Lighting",
    "consumption": 0.1362222223,
    "possibleHours":
        [0, 1, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 22, 23],
    "hoursOn": 19,
    "consecutiveHours": 19
}
D9 = {
    "name": "Refrigerator",
    "consumption": 0.14,
    "possibleHours":
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
    "hoursOn": 24,
    "consecutiveHours": 24
}
# - 0 , 1 ,2 ,3 ,4 ,5 ,6 ,7 ,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23
# D0 AC - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
# D1 DishWasher - [12, 13, 14, 19, 20, 21]
# D2 WashingMachine - [0, 1, 2, 3, 4, 5, 6, 15, 16, 17, 22, 23]
# D3 Dryer - [0, 1, 2, 3, 4, 5, 6, 15, 16, 17, 22, 23]
# D4 WaterHeater - [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# D5 TV - [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
# D6 Microwave - [7, 8, 12, 13, 19, 20]
# D7 Kettle -  [6, 7, 8, 12, 13, 17, 18, 19, 20, 22]
# D8 Lighting - [0, 1, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 22, 23]
# D9 Refrigerator - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

# Microwave -> Dishwasher D6->D1
# WashingMachine -> Dryer D2 -> D3


#real device 1
# [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],


precedences = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

]


def getDevices():
    return [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9]


def getPrecedences():
    return precedences

def getConsumptions():
    c=[]
    for k, v in consumptions.items():
        c.append(v)
    return c

