import pandas as pd 
import matplotlib.pyplot as plt

'''This shows a scatter plot with two data points that are singled out because I wanted to find the film with the highest
Opening Gross and the film with the highest Opening Gross but that only been shown in less than 4000 theaters '''

df = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 2\Movies2016.xlsx",sheet_name="Sheet1")

y_axis = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 2\Movies2016.xlsx",usecols=["Opening Gross Sales ($ millions)"])

x_axis = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 2\Movies2016.xlsx", usecols=["Number of Theaters"])



max_value = y_axis['Opening Gross Sales ($ millions)'].max()

df.plot(kind='scatter',x='Number of Theaters',y='Opening Gross Sales ($ millions)')
# Iterate through the DataFrame
for index, row in df.iterrows():

    current_value = row["Opening Gross Sales ($ millions)"]
    if current_value == max_value:
        movie_title= row["Movie Title"]
less_4000 = []
for index, row in df.iterrows():
    
    current_value = row["Opening Gross Sales ($ millions)"]
    if row["Number of Theaters"] < 4000:
        less_4000.append(current_value)


maxofless4000=max(less_4000)

for index, row in df.iterrows():
    current_value = row["Opening Gross Sales ($ millions)"]
    if current_value==maxofless4000:
        label_2ndcond = row["Movie Title"]
        break

i = 0 
when = []
for index, row in df.iterrows():
    if label_2ndcond == row["Movie Title"]:
       
        when.append(i)
        i+= 1
    if movie_title  == row["Movie Title"]:
   
        when.append(i)  
        i+= 1
    else:
        i+= 1

for i in when:
    plt.text(df["Number of Theaters"][i] + 0.5, df["Opening Gross Sales ($ millions)"][i] + 0.5, df["Movie Title"][i], fontsize=9, ha='left', va='bottom')




        





plt.xlabel('Number of Theaters')
plt.ylabel('Opening Gross Sales ($ millions)')
plt.show()


