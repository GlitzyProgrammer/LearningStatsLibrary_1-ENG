import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns  # for heatmap styling
import numpy as np
from scipy.stats import skew

df = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 3\Movies2016.xlsx",sheet_name="Sheet1")

df['Opening Gross Sales ($ millions)']=  pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 3\Movies2016.xlsx",usecols=['Opening Gross Sales ($ millions)'])
df["Number of Theaters"] = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 3\Movies2016.xlsx",usecols=["Number of Theaters"])
df["Total Gross Sales ($ millions)"] = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 3\Movies2016.xlsx",usecols=["Total Gross Sales ($ millions)"])
df["Weeks in Release"]= pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 3\Movies2016.xlsx",usecols=["Weeks in Release"])
#Descriptive Statstics 

kurt_OP_Gross =  df['Opening Gross Sales ($ millions)'].astype(int)  # converts data to int type for smooth kurtosis caluation
kurt_Num_theater=  df["Number of Theaters"].astype(int)
kurt_Total_Gross =  df["Total Gross Sales ($ millions)"].astype(int)
kurt_Weeks=df["Weeks in Release"].astype(int)
kurtosis_data = [kurt_OP_Gross,kurt_Num_theater,kurt_Total_Gross,kurt_Weeks]
labels = ['Opening Gross Sales ($ millions)',"Number of Theaters","Total Gross Sales ($ millions)","Weeks in Release"]

def custom_describe(data):
    description = data.describe()
    description.loc['Kurtosis'] = data.kurtosis()
    description.loc['Sample Variation'] = description.loc['std'] **2   
    description.loc['Standard Error'] = description.loc['std'] / description.loc['count']
    ske_1 = description.loc['count'].astype(int)/(description.loc['count'].astype(int)-1)*(description.loc['count'].astype(int)-2)
    ske_2 = np.sum(((data.astype(int) - description.loc['mean'].astype(int)) / description.loc['std'].astype(int)))
    #multiplying the difference between mean and median by three and dividing by the standard deviation.
    # [n/(n-1)(n-2)] * Σ[(xi–x)/s]3
    description.loc['Skewness'] =  skew(data)
    description.loc["Sum"] = sum(data)
    description.loc['Range']= description.loc['max'].astype(int)-description.loc['min'].astype(int)
    description =description.rename(index={'25%': 'Mode', '50%': 'Median','max':'Maximum','min':'Minimum','std':'Standard Deviation','mean':'Mean','count':'Count'})
    description = description.drop("75%")
    new_order = ['Mean', 'Standard Error', 'Median','Mode','Standard Deviation','Sample Variation',"Kurtosis","Skewness","Range","Minimum","Maximum","Sum","Count"]
    description = description.reindex(new_order)
    return description
#def custom_describe(df):
 #    description = df.describe()
  #   description.loc['kurtosis'] = df.kurtosis()
   #  return description
for i in range(len(kurtosis_data)):      #printing out descriptive stats
    print(f"This is {labels[i]}'s Description of Statstics\n")
    print(custom_describe(kurtosis_data[i]))
    print("\n")


#Calculate kurtosis using Pearson's definition (bias=False)

#print(df.info())


#print(f"Fisher's Kurtosis: {kurtosis_fisher}")
#print(f"Pearson's Kurtosis: {kurtosis_pearson}")