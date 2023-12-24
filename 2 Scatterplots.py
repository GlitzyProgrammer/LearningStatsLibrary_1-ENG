import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 3\Movies2016.xlsx",sheet_name="Sheet1")

df['Opening Gross Sales ($ millions)']=  pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 3\Movies2016.xlsx",usecols=['Opening Gross Sales ($ millions)'])
df["Number of Theaters"] = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 3\Movies2016.xlsx",usecols=["Number of Theaters"])
df["Total Gross Sales ($ millions)"] = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 3\Movies2016.xlsx",usecols=["Total Gross Sales ($ millions)"])
df["Weeks in Release"]= pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 3\Movies2016.xlsx",usecols=["Weeks in Release"])


#Opening gross sales vs. Number of theaters
x_axis = df["Number of Theaters"].astype(int)
y_axis = df['Opening Gross Sales ($ millions)'].astype(int)

correlation_coefficient = df["Number of Theaters"].astype(int).corr(df['Opening Gross Sales ($ millions)'].astype(int))


df.plot(kind='scatter',x="Number of Theaters",y='Opening Gross Sales ($ millions)')
plt.ylim(bottom=0)  # regression makes it neagtive ranges
y_ticks = plt.yticks()[0]
y_ticks.ptp()
for y_tick in y_ticks:
    if y_tick < 0:
        continue
    else:
      plt.axhline(y=y_tick, color='black', linestyle='-', alpha=0.1)
fit = np.polyfit(df["Number of Theaters"], df['Opening Gross Sales ($ millions)'], 1)
regression_line = np.poly1d(fit)
plt.plot(df["Number of Theaters"], regression_line(df["Number of Theaters"].astype(int)), color='red', label=f'R = {correlation_coefficient:.2f}')

plt.xlabel("Number of Theaters")
plt.ylabel('Opening Gross Sales ($ millions)')
plt.legend()
plt.xlim(0, 5000)
plt.show()
#Total gross sales vs. Weeks in release

x_axis = df["Weeks in Release"].astype(int)
y_axis = df["Total Gross Sales ($ millions)"].astype(int)

correlation_coefficient = df["Weeks in Release"].astype(int).corr(df["Total Gross Sales ($ millions)"].astype(int))

df.plot(kind='scatter',x="Weeks in Release",y="Total Gross Sales ($ millions)")
fit = np.polyfit(df["Weeks in Release"], df["Total Gross Sales ($ millions)"], 1)

#Adds y-axis lines to the scatter plot 
y_ticks = plt.yticks()[0]
for y_tick in y_ticks:
    if y_tick < 0:
        continue
    else:
      plt.axhline(y=y_tick, color='black', linestyle='-', alpha=0.1)

regression_line = np.poly1d(fit)
plt.plot(df["Weeks in Release"].astype(int), regression_line(df["Weeks in Release"].astype(int)), color='red', label=f'R = {correlation_coefficient:.2f}')

plt.xlabel("Weeks in Release")
plt.ylabel("Total Gross Sales ($ millions)")
plt.legend()
plt.xlim(0, 50)
plt.show()

