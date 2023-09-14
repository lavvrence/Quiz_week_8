import matplotlib.pyplot as plt
import pandas as pd

# reading climate csv file
climate = pd.read_csv('climate.csv')

# using column names to create series for each column in the csv file
years = climate['Year']
co2 = climate['CO2']
temp = climate["Temperature"]

#plotting
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 

