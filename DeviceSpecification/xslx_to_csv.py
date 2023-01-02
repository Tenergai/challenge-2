# importing pandas as pd
import pandas as pd

# Read and store content
# of an excel file
#read_file = pd.read_excel("Consumer1.xlsx")

# Write the dataframe object
# into csv file
#read_file.to_csv("Consumer1.csv",index=None,header=True)

# read csv file and convert
# into a dataframe object
df = pd.DataFrame(pd.read_csv("Consumer1.csv"))

# show the dataframe
#print(df)

df.index // 5

df.groupby(df.index // 5).sum()

print(df)


#df.set_index(df.index // 4).sum(level=0)
#print(df)


## Get sum of first 2 rows of DataFrame
#sum = df.iloc[0:2].sum()
#print(sum)
