import numpy as np

price = np.random.rand(24)
#print(price)

generation = np.random.randint(10, size=24)
#print(generation)

devices = np.random.randint(2, size=(10, 24))
#print(devices)

consumption = np.random.rand(10,24)
#print(consumption)

def multiply_arrays(a, b):
  return [x * y for x, y in zip(a, b)]


def calculateConsumption(hour):
    devicesOnThatHour = devices[:, hour];
    consumptionOnThatHour = consumption[:,hour];
    #print(devicesOnThatHour)
    #print(consumptionOnThatHour)
    result = multiply_arrays(devicesOnThatHour,consumptionOnThatHour)
    #print("result")
    #print(result)
    #print("#################")
    return sum(result)


def objectiveFunction():
    profit = np.zeros(24)
    for h in range(24):
        consumptionHour = calculateConsumption(h);
        #print("cosumptionHour")
        #print(consumptionHour)
        profit[h] = price[h] * (generation[h]*consumptionHour);

    totalProfit = sum(profit)
    return profit, totalProfit

p,total= objectiveFunction()
print(p)
print(total)

#calculateConsumption(0)