import pandas as pd 
import matplotlib.pyplot as plt



df = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 2\Movies2016.xlsx",sheet_name="Sheet1")

y_axis = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 2\Movies2016.xlsx",usecols=["Opening Gross Sales ($ millions)"])

x_axis = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 2\Movies2016.xlsx", usecols=["Number of Theaters"])


less_4000 = []
max_value = y_axis['Opening Gross Sales ($ millions)'].max()

df.plot(kind='scatter',x='Number of Theaters',y='Opening Gross Sales ($ millions)')

#This iterates among the index of the dataframe looking for the "Opening Gross Sales"  row  and finds the corresponding Movie Title 
for index, row in df.iterrows():
    current_value = row["Opening Gross Sales ($ millions)"]
    if current_value == max_value:
        highest_title= row["Movie Title"]

#This iterates among the index of the dataframe looking for the "Opening Gross Sales"  row 
# It gathers information for the number of theaters less than 4000
for index, row in df.iterrows():
    current_value = row["Opening Gross Sales ($ millions)"]
    if row["Number of Theaters"] < 4000:
        less_4000.append(current_value)
        
maxofless4000=max(less_4000)

#This iterates among the index of the dataframe looking for the "Opening Gross Sales"  row  trying to find the title that corresponds with a "Movie Title"
for index, row in df.iterrows():
    current_value = row["Opening Gross Sales ($ millions)"]
    if current_value==maxofless4000:   
        label_2ndcond = row["Movie Title"]
        break


found_title = []   
for index, row in df.iterrows():
    if label_2ndcond == row["Movie Title"]:
        found_title.append(index)
        
    if highest_title  == row["Movie Title"]:
        found_title.append(index)  

# Place the titles on the scatter plot 
for i in found_title:
    plt.text(df["Number of Theaters"][i] + 0.5, df["Opening Gross Sales ($ millions)"][i] + 0.5, df["Movie Title"][i], fontsize=9, ha='left', va='bottom')



plt.xlabel('Number of Theaters')
plt.ylabel('Opening Gross Sales ($ millions)')
plt.show()


