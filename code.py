import pandas as pd
data= pd.read_excel(r'Path\to\dataset.xlsx')
print(data)

import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
import statistics

#the plot

fig, ax = plt.subplots(figsize=(15, 8))

ax.set_ylabel("Performance Ratio[%]")
ax.set_xlabel("Date")
ax.set_ylim(0, 100)
ax.yaxis.set_major_locator(MultipleLocator(10))
ax.grid(which='both')

#the scatter points depicting the GHI    

nav_blu=[]
lig_blu=[]
org=[]
br=[]

nav_blu = data.loc[data['GHI']<2]
lig_blu = data.loc[(data['GHI']>=2) & data['GHI']<4]
org = data.loc[(data['GHI']>=4) & data['GHI']<=6]
br = data.loc[data['GHI']>6]

ax.scatter(nav_blu['Date'],nav_blu['PR'] , c ="blue",s=35,marker ="s")
ax.scatter(lig_blu['Date'],lig_blu['PR'] , c ="tab:cyan",s=45,marker ="^")
ax.scatter(org['Date'],org['PR'] , c ="tab:orange",s=15)
ax.scatter(br['Date'],br['PR'] , c ="tab:brown",s=15)

ax.scatter(x_line[200],96 , c ="blue",s=35,marker ="s")
plt.text(x_line[212],95.4,"<2")
ax.scatter(x_line[300],96 , c ="tab:cyan",s=45,marker ="^")
plt.text(x_line[312],95.4,"2-4")
ax.scatter(x_line[400],96, c ="tab:orange",s=15)
plt.text(x_line[412],95.4,"4-6")
ax.scatter(x_line[500],96, c ="tab:brown",s=15)
plt.text(x_line[512],95.4,">6")

#the budget line

y_line=[]
x_line=[]
initial = 73.9
initial_year=2019
for date in data['Date']:
    x_line.append(date)
    if date.year== initial_year+1:
        initial_year=initial_year+1
        initial -= initial*0.8/100    
    y_line.append(initial)

ax.plot(x_line,y_line,c="green",linewidth=2.3)

#the 30-d moving average of the PR (Performance Evolution)

means=[]
date_mean=[]
for i in range(0,981):
    date_mean.append(data['Date'][i])
    new_arr=data['PR'][i:i+30:1]
    i=i+30
    mean_one = statistics.mean(new_arr)
    means.append(mean_one)

ax.plot(date_mean,means,c="red",linewidth=2.3)

plt.text(x_line[0],95,"Daily Irradiation[kWh/m2]")

#average PR for the last 7 days, the last 30 days, last 60 days, etc.

avg_7=statistics.mean(data['PR'].tail(7))
avg_30=statistics.mean(data['PR'].tail(30))
avg_60=statistics.mean(data['PR'].tail(60))
avg_90=statistics.mean(data['PR'].tail(90))
avg_365=statistics.mean(data['PR'].tail(365))

plt.text(x_line[700],33,"Avg PR last 7-d:")
plt.annotate(str(avg_7), xy=(x_line[815], 33))
plt.text(x_line[700],27,"Avg PR last 30-d:")
plt.annotate(str(avg_30), xy=(x_line[815], 27))
plt.text(x_line[700],21,"Avg PR last 60-d:")
plt.annotate(str(avg_60), xy=(x_line[815], 21))
plt.text(x_line[700],15,"Avg PR last 90-d:")
plt.annotate(str(avg_90), xy=(x_line[815], 15))
plt.text(x_line[700],9,"Avg PR last 365-d:")
plt.annotate(str(avg_365), xy=(x_line[818], 9))
