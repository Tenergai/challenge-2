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
#Device
#   Name, Consumption, Possible Hours, Hours On, Consecutive Hours

D1 = {
    "AC",
    0.3299995377,
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],
    [2],
    [2]
}



def getDeviceConsumption():
    return consumptions
