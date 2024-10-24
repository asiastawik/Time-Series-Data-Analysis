import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

#TASK 2
path = os.path.join('data', 'a10.csv')
data = pd.read_csv('data/a10.csv', parse_dates=True, index_col=0)
#data = data.set_index('Month')
#print(data)

cost = data.Cost
plt.plot(cost)
plt.show()

#TASK 3
Q_data_min = data.resample('Q').min()
#print(Q_data_min)
plt.plot(Q_data_min.Cost)
plt.show()

Q_data_Y_min = data.resample('Y').min()
Q_data_Y_max = data.resample('Y').max()
Q_data_Y_mean = data.resample('Y').mean()
plt.plot(Q_data_Y_min.Cost)
plt.plot(Q_data_Y_max.Cost)
plt.plot(Q_data_Y_mean.Cost)
plt.legend(['min', 'max', 'mean'])
plt.show()

#TASK 4
data_1 = pd.read_csv('data/a10.csv', parse_dates=False, index_col=0)
print(data_1)
years = []
for i in data_1.index:
    year = i.split()[0]
    if year not in years:
        years.append(year)

print(years)

#years = sorted(list(set(e.split()[0] for e in data_1.index)))

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

total_costs = {} # create a dictionary
for y in years:
    total_costs[y] = []
    for m in months:
        if f'{y} {m}' in data_1.index:
            year_month_cost = data_1.loc[data_1.index == f'{y} {m}', 'Cost'].to_numpy().sum()
            total_costs[y].append(year_month_cost)
        else:
            total_costs[y].append(np.nan)

# Create a plot with lines for each year
fig, ax = plt.subplots()
for y in years:
    ax.plot(months, total_costs[y], label=y)

ax.set_xlabel('Month')
ax.set_ylabel('Total Cost')
ax.set_title('Total Costs by Year-Month')
ax.legend()
plt.show()