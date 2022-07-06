import pandas as pd
import matplotlib.pyplot as plt

pandas_csv = pd.read_csv('housing.csv')

head = pandas_csv.head()
headers = pandas_csv.columns

print(head)
print(headers)

new = pandas_csv[['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'population', 'households']]

plt.plot(pandas_csv['total_rooms'], pandas_csv['housing_median_age'])
