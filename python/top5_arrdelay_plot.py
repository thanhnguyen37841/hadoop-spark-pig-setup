import glob
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

all_rec = glob.glob("/home/hadoopuser/q_carrier_best5_arr/part*")
dataframes = [pd.read_csv(f, sep=",", header=None) for f in all_rec]
df = pd.concat(dataframes, ignore_index=True)
df.columns = ['Carrier', 'AvgArr']
df = df.sort_values('AvgArr').head(5)
print(df)

ax = df.plot(x='Carrier', y='AvgArr', kind='bar', figsize=(10,5), color='steelblue')
ax.set_title("Top 5 Hang Bay co ArrDelay Trung Binh Thap Nhat")
ax.set_xlabel("Hang Bay")
ax.set_ylabel("Avg Arrival Delay (phut)")
plt.tight_layout()
plt.savefig('/home/hadoopuser/top5_arr_delay_chart.png', dpi=150)
print("Da luu top5_arr_delay_chart.png")
