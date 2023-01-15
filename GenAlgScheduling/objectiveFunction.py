import numpy as np
from deviceSpecification import getDevices,getConsumptions
from generateMatrix import generateMatrix
from utils import getPricesForToday,getDailyGeneration

devices = getDevices()
devicesHourly = generateMatrix(devices)
price = getPricesForToday()

generation = getDailyGeneration()
r=len(generation)
c=len(getDevices())
consumption = getConsumptions()

def multiply_arrays(a, b):
    return [x * y for x, y in zip(a, b)]


def calculateConsumption(devicesHourly,hour):
    devicesOnThatHour = devicesHourly[:, hour]
    consumptionOnThatHour = consumption
    result = multiply_arrays(devicesOnThatHour, consumptionOnThatHour)
    return sum(result)


def objectiveFunction(profit,devicesHourly):
    t=[] 
    for devices in devicesHourly:
        device=devices[0]
        sc=devices[1]
        profit = np.zeros(r)
        for h in range(r):
            consumptionHour = calculateConsumption(device,h)
            profit[h] = price[h] * (generation[h] * consumptionHour)
        totalProfit = sum(profit)
        totalProfit=totalProfit/sc
        t.append(totalProfit)
    return t

