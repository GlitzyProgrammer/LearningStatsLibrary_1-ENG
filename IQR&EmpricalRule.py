import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 3\Movies2016.xlsx",sheet_name="Sheet1")

df['Opening Gross Sales ($ millions)'] =  pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 3\Movies2016.xlsx",usecols=['Opening Gross Sales ($ millions)'])
df["Total Gross Sales ($ millions)"] = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 3\Movies2016.xlsx",usecols=["Total Gross Sales ($ millions)"])

#IQR caluation 

# Opening Gross Sales 

q1 = df['Opening Gross Sales ($ millions)'].quantile(0.25)
q3 = df['Opening Gross Sales ($ millions)'].quantile(0.75)
iqr = q3-q1
Upper_EMP = q3+(1.5*iqr)
Lower_EMP =  q1-(1.5*iqr)
print('Opening Gross Sales ($ millions) Lower & Upper Limits also Emperical Rule ')
print("Lower Limit",round(q1,7))
print("Upper Limit :",round(q3,7))
print("IQR:",round(iqr,7))
print("Upper Emp Rule",round(Upper_EMP,7))
print("Lower Emp Rule",round(Lower_EMP,7))
print(" ")
print(" ")


# Total Gross Sales 
q1 = df["Total Gross Sales ($ millions)"].quantile(0.25)
q3 = df["Total Gross Sales ($ millions)"].quantile(0.75)
iqr = q3-q1
Upper_EMP = q3+(1.5*iqr)
Lower_EMP =  q1-(1.5*iqr)
print('Total Gross Sales ($ millions) Lower & Upper Limits also Emperical Rule')
print("Lower Limit",round(q1,7))
print("Upper Limit :",round(q3,7))
print("IQR:",round(iqr,7))
print("Upper Emp Rule",round(Upper_EMP,7))
print("Lower Emp Rule",round(Lower_EMP,7))



