import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns  # for heatmap styling
import numpy as np

df = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 2\Movies2016.xlsx",sheet_name="Sheet1")

df_yaxis = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 2\Movies2016.xlsx",usecols=["Total Gross Sales ($ millions)"])
df_xaxis = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 2\Movies2016.xlsx", usecols=["Number of Theaters"])

bins_y = [0,30,60,90,120,150,180,np.inf]
labels_y = ['0-30','30-60','60-90','90-120','120-150','150-180','170-180','180-beyond']

bins_x = [1000,2000,3000,4000,5000]
labels_x= ['1000-1999','2000-2999','3000-3999','4000-5000']

df['Numbers of Theaters'] = pd.cut(df["Number of Theaters"],bins=bins_x)
df['Total Gross Sales ($ millions)'] = pd.cut(df["Total Gross Sales ($ millions)"],bins=bins_y)
cross_table = pd.crosstab(df['Numbers of Theaters'],df['Total Gross Sales ($ millions)'] ,margins=True, margins_name='Grand Total')
fig, ax = plt.subplots(figsize=(14, 10))
plt.imshow(cross_table, cmap='YlGnBu', interpolation='nearest')
plt.yticks(np.arange(len(cross_table.index) ), cross_table.index)

plt.tick_params(axis='x', which='both', bottom=False, top=True)

plt.xticks(np.arange(len(cross_table.columns) ), cross_table.columns,rotation=45, ha='right') 

for i in range(len(cross_table.index)):
    for j in range(len(cross_table.columns)):
        plt.text(j, i, str(cross_table.iloc[i, j]), ha='center', va='center', color='black')
plt.colorbar()
plt.title('Opening Gross Sales ($ millions) vs. the number of theaters')
plt.show()



