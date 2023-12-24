import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 2\Movies2016.xlsx",sheet_name="Sheet1")

y_axis = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 2\Movies2016.xlsx",usecols=["Total Gross Sales ($ millions)"])

x_axis = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 2\Movies2016.xlsx", usecols=["Weeks in Release"])
  
max_value_TGS = y_axis["Total Gross Sales ($ millions)"].max()
max_value_long= x_axis["Weeks in Release"].max()

df.plot(kind='scatter',x="Weeks in Release",y="Total Gross Sales ($ millions)")
#This iterates among the index of the dataframe looking for the "Total Gross Sales ($ millions)"  row  and finds the corresponding Movie Title 
for index, row in df.iterrows():
    current_value = row["Total Gross Sales ($ millions)"]
    if current_value == max_value_TGS:
        movie_title= row["Movie Title"]
        print(movie_title, current_value)
        break

#This iterates among the index of the dataframe looking for the"Weeks in Release"  row  and finds the corresponding Movie Title 
for index, row in df.iterrows():
    current_value = row["Weeks in Release"]
    if current_value == max_value_long:
        movie_title_2= row["Movie Title"]
        print(movie_title_2, current_value)
        break



found_title = []
#Iterates through the dataframe's index trying to find the two movie titles that were found earlier 
for index, row in df.iterrows():
    if movie_title_2 == row["Movie Title"]: 
        found_title.append(index)
      
    if movie_title  == row["Movie Title"]:
        found_title.append(index)  

for i in found_title:
    plt.text(df["Weeks in Release"][i] + 0.5, df["Total Gross Sales ($ millions)"][i] + 0.5, df["Movie Title"][i], fontsize=9, ha='left', va='bottom')

plt.xlabel("Weeks in Relase")
plt.ylabel("Total Gross Sales ($ millions)")
plt.show()
