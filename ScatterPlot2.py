import pandas as pd 
import matplotlib.pyplot as plt
'''This shows a scatter plot with two data points that are singled out because I wanted to find the film with the highest
Total Gross and the film that was in the theaters the longest '''
df = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 2\Movies2016.xlsx",sheet_name="Sheet1")

y_axis = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 2\Movies2016.xlsx",usecols=["Total Gross Sales ($ millions)"])

x_axis = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 2\Movies2016.xlsx", usecols=["Weeks in Release"])
  
max_value_TGS = y_axis["Total Gross Sales ($ millions)"].max()
max_value_long= x_axis["Weeks in Release"].max()

df.plot(kind='scatter',x="Weeks in Release",y="Total Gross Sales ($ millions)")
for index, row in df.iterrows():

    current_value = row["Total Gross Sales ($ millions)"]
    if current_value == max_value_TGS:
        movie_title= row["Movie Title"]
        print(movie_title, current_value)
        break

for index, row in df.iterrows():

    current_value = row["Weeks in Release"]
    if current_value == max_value_long:
        movie_title_2= row["Movie Title"]
        print(movie_title_2, current_value)
        break


i = 0 
when = []
for index, row in df.iterrows():
    if movie_title_2 == row["Movie Title"]:
       
        when.append(i)
        i+= 1
    if movie_title  == row["Movie Title"]:
   
        when.append(i)  
        i+= 1
    else:
        i+= 1

for i in when:
    plt.text(df["Weeks in Release"][i] + 0.5, df["Total Gross Sales ($ millions)"][i] + 0.5, df["Movie Title"][i], fontsize=9, ha='left', va='bottom')

plt.xlabel("Weeks in Relase")
plt.ylabel("Total Gross Sales ($ millions)")
plt.show()