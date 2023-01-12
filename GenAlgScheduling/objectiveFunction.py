import numpy as np
from utils import getPricesForToday,getDailyGeneration
price = getPricesForToday()
#np.random.rand(24)
# print(price)

generation = np.random.randint(10, size=24)#getDailyGeneration()
# print(generation)

# devices = np.random.randint(2, size=(10, 24))
# print('check',devices)

consumption = np.random.rand(10, 24)

profit = np.zeros(24)


# print(consumption)

def multiply_arrays(a, b):
    return [x * y for x, y in zip(a, b)]


def calculateConsumption(devices,hour):
    devicesOnThatHour = devices[:, hour]
    consumptionOnThatHour = consumption[:, hour]
    # print(devicesOnThatHour)
    # print(consumptionOnThatHour)
    result = multiply_arrays(devicesOnThatHour, consumptionOnThatHour)
    # print("result")
    # print(result)
    # print("#################")
    return sum(result)


def objectiveFunction(profit,ind,devices):
    profit = np.zeros(24)
    for h in range(24):
        consumptionHour = calculateConsumption(devices,h)
        # print("cosumptionHour")
        # print(consumptionHour)
        profit[h] = price[h] * (generation[h] * consumptionHour)
    totalProfit = sum(profit)
    return totalProfit


# p, total = objectiveFunction()
# print(p)
# print(total)

# calculateConsumption(0)
