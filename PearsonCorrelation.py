import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
import itertools 
df = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 3\Movies2016.xlsx",sheet_name="Sheet1")



df['Opening Gross Sales ($ millions)'] =  pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 3\Movies2016.xlsx",usecols=['Opening Gross Sales ($ millions)'])
df["Total Gross Sales ($ millions)"] = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 3\Movies2016.xlsx",usecols=["Total Gross Sales ($ millions)"])
df['Number of Theaters']= pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 3\Movies2016.xlsx",usecols=['Number of Theaters'])
df['Weeks in Realse'] = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 3\Movies2016.xlsx",usecols=['Weeks in Release'])

Opening_Gross = df['Opening Gross Sales ($ millions)']
Total_Gross = df["Total Gross Sales ($ millions)"] 
Num_Theaters =df['Number of Theaters']
Weeks_In_Real =df['Weeks in Realse']

colums = [Opening_Gross,Total_Gross,Num_Theaters,Weeks_In_Real]
dataframes = {'Opening Gross Sales ($ millions)': df['Opening Gross Sales ($ millions)'],
               "Total Gross Sales ($ millions)": df["Total Gross Sales ($ millions)"],
               'Number of Theaters':df['Number of Theaters'],
               'Weeks in Realse':df['Weeks in Realse']}

def pariwise_cor_pearson(dataframes):
     for pair in itertools.combinations(dataframes, 2): 
             element1, element2 = pair 
             dataframes[element1] 
             
             corr_matrix = np.corrcoef(dataframes[element1] ,dataframes[element2] )
             corr_coefficient = corr_matrix[0, 1]
             print(f"This is the Pearson Correlaiton Coefficient for {element1} and {element2} is  {round(corr_coefficient,3)}")
            
pariwise_cor_pearson(dataframes)