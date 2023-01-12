import numpy as np
from deviceSpecification import getDevices
from generateMatrix import generateMatrix
from utils import getPricesForToday,getDailyGeneration
price = getPricesForToday()

generation = getDailyGeneration()

consumption = np.random.rand(10, 24)

profit = np.zeros(24)


def multiply_arrays(a, b):
    return [x * y for x, y in zip(a, b)]


def calculateConsumption(devicesHourly,hour):
    devicesOnThatHour = devicesHourly[:, hour]
    consumptionOnThatHour = consumption[:, hour]
    result = multiply_arrays(devicesOnThatHour, consumptionOnThatHour)
    return sum(result)


def objectiveFunction(profit,devicesHourly):
    profit = np.zeros(24)
    for h in range(24):
        consumptionHour = calculateConsumption(devicesHourly,h)
        profit[h] = price[h] * (generation[h] * consumptionHour)
    totalProfit = sum(profit)
    return totalProfit

