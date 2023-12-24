import pandas as pd 



df = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 2\Movies2016.xlsx",sheet_name="Sheet1")


y_axis = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 2\Movies2016.xlsx",usecols=["Total Gross Sales ($ millions)"])

x_axis = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 2\Movies2016.xlsx", usecols=["Weeks in Release"])
y_axis = y_axis.astype(float)
bins_y = [20,120,220,320,420,520,620]
bins_x = [5,25,30,50]

#Changed the orignal x-axis bins because the way that cross tab does bins goes infintly inbetween points
#It also ignored some ibetween values in the bins suggested automatically

print(len(df['Weeks in Release']))
df["Weeks in Release"]=pd.cut(df["Weeks in Release"],bins=bins_x)
df["Total Gross Sales ($ millions)"]=pd.cut(df["Total Gross Sales ($ millions)"],bins=bins_y, right=True)


cross_table = pd.crosstab(df["Total Gross Sales ($ millions)"],df["Weeks in Release"] ,margins=True, margins_name='Grand Total')
print(cross_table)





