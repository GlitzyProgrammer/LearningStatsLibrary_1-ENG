import pandas as pd 
import numpy as np

df = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 2\Movies2016.xlsx",sheet_name="Sheet1")

Op_sales = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 2\Movies2016.xlsx",usecols=["Opening Gross Sales ($ millions)"])

bin_sales=[0,100,np.inf]

x_axis_labels = [' Over $100M for Opening Gross Sales',	' Under $100M for Opening Gross Sales']
y_axis_labels = ['SuperHero',"non-Suphero"]

superhero = ['X-Men Apocalypse', 'Doctor Strange', 'Deadpool', 'Suicide Squad', 'Batman v Superman: Dawn of Justice', 'Captain America: Civil War']


print(" ")
#This point I filtered out movies in general that had Opening Gross Sales over 50 million dollars
print("The following movies had an Opening Gross Sales more than 50 million")
more_50mil = {"Movie Title":[],
              "Opening Gross Sales ($ millions)":[]}

#Iterating through the index of the dataframe for the Opening Gross Sales
for index, row in df.iterrows():
    current_value = row["Opening Gross Sales ($ millions)"]
    if current_value > 50:
           more_50mil['Movie Title'].append(row["Movie Title"])
           more_50mil['Opening Gross Sales ($ millions)'].append(row['Opening Gross Sales ($ millions)'])
        
fiftymillion_df = pd.DataFrame(more_50mil)
fifymillion_sorted = fiftymillion_df.sort_values(by='Opening Gross Sales ($ millions)')  
#This sorted the dataframe in ascending order
print(fiftymillion_df)
print("\n")
print("Proof of sorting\n")
print(fifymillion_sorted)
print("\n")
print("Cross Tab of  relative success\n")


#This one is a custom crosstabulation of the relative sucess of Superhero and Non-suphero movies being over or under 100 million dollars
u_left= 0
u_right=0
l_left = 0
l_right = 0
# This iterates through the fifymillion_sorted dataframe searching for "Moive Title" and "Opening Gross Sales" 
for index, row in fifymillion_sorted.iterrows():
      if row['Movie Title'] in superhero and row["Opening Gross Sales ($ millions)"]>100:   #greater than 100 and suphero
           u_left +=1
      elif row['Movie Title'] in superhero and row["Opening Gross Sales ($ millions)"]<100:  #less than 100 and suphero
            u_right+=1
            
      elif not(row['Movie Title'] in superhero) and row["Opening Gross Sales ($ millions)"]<100:
            l_right +=1              #non suphero and less than 100
      elif not(row['Movie Title'] in superhero) and row["Opening Gross Sales ($ millions)"]>100:
            l_left+= 1
super_hero = {"# Over $100M for Opening Gross Sales":[],
              "# Under $100M for Opening Gross Sales":[]}		
labels = ['Superhero','Not Superhero']
super_hero['# Over $100M for Opening Gross Sales'].append(u_left)
super_hero['# Over $100M for Opening Gross Sales'].append(l_left)
super_hero['# Under $100M for Opening Gross Sales'].append(u_right)
super_hero['# Under $100M for Opening Gross Sales'].append(l_right)
df_supher_hero = pd.DataFrame(super_hero)
df_supher_hero = df_supher_hero .rename(index={0: labels[0], 1: labels[1]})
print(df_supher_hero)
