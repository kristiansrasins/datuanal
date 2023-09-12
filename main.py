from matplotlib import pyplot as plt
import pandas as pd

# Set figure size and autolayout
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

# Read the CSV file
columns = ["Datetime", "x", "y", "z", "sum"]
df = pd.read_csv("user_acceleration.csv", usecols=columns)

# Convert the "Datetime" column to datetime format
df['Datetime'] = pd.to_datetime(df['Datetime'])

# Group the data by 1-second intervals and calculate the average of the "sum" column
df_1s_avg = df.resample('3S', on='Datetime').mean().reset_index()

# Create a plot for the 1-second average
plt.plot(df_1s_avg['Datetime'], df_1s_avg['sum'])
plt.xlabel('Time')
plt.ylabel('1-Second Average Sum')
plt.title('1-Second Average Sum vs. Time')
plt.grid(True)
plt.show()
