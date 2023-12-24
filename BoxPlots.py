import pandas as pd 
import matplotlib.pyplot as plt


df = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 3\Movies2016.xlsx",sheet_name="Sheet1")

df['Opening Gross Sales ($ millions)'] =  pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 3\Movies2016.xlsx",usecols=['Opening Gross Sales ($ millions)'])
df["Total Gross Sales ($ millions)"] = pd.read_excel(r"C:\Users\ljwil\Desktop\Intro STATS\Project Stats 2\Chapter 3\Movies2016.xlsx",usecols=["Total Gross Sales ($ millions)"])



plot= df['Total Gross Sales ($ millions)']
#Adds the mean plot to the boxplot
plot_mean = plot.mean()
out=plt.boxplot(plot,meanline=True,showfliers=True, flierprops=dict(markerfacecolor='pink', marker='o'),patch_artist=True)
target_box_color='chartreuse'
out['boxes'][0].set_facecolor(target_box_color)
plt.plot( 1,plot_mean, 'rx', markersize=10)
y_ticks = plt.yticks()[0]

# Add vertical lines at each y-axis tick
for y_tick in y_ticks:
    if y_tick < 0:
        continue
    else:
      plt.axhline(y=y_tick, color='black', linestyle='-', alpha=0.5)

plt.xticks([])
plt.ylabel('Total Gross Sales ($ millions)')
plt.show()



plot= df['Opening Gross Sales ($ millions)']
#Adds the mean plot to the boxplot
plot_mean = plot.mean()
out=plt.boxplot(plot,meanline=True,showfliers=True, flierprops=dict(markerfacecolor='pink', marker='o'),patch_artist=True)
target_box_color='chartreuse'
out['boxes'][0].set_facecolor(target_box_color)
plt.plot( 1,plot_mean, 'rx', markersize=10)
y_ticks = plt.yticks()[0]

# Add vertical lines at each y-axis tick
for y_tick in y_ticks:
    if y_tick < 0:
        continue
    else:
      plt.axhline(y=y_tick, color='black', linestyle='-', alpha=0.5)

plt.xticks([])
plt.ylabel('Opening Gross Sales ($ millions)')
plt.show()
