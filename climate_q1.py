import sqlite3
import matplotlib.pyplot as plt

#connect to database
con = sqlite3.connect('climate.db')
cursor = con.cursor()


# query for retrieving data
cursor.execute("SELECT * FROM ClimateData")

years = []
co2 = []
temp = []

# sorting data from query
for row in cursor.fetchall():
    years.append(row[0])
    co2.append(row[1])
    temp.append(row[2])

# close connection
con.close()

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
plt.savefig("co2_temp_1.png") 
