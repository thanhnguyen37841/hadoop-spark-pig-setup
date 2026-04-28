
import glob
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

data_path = "/home/hadoopuser/q_month_delay_rate/part*"
all_rec = glob.glob(data_path)

if len(all_rec) == 0:
    print("Khong tim thay du lieu tai q_month_delay_rate")
    exit()

dataframes = [pd.read_csv(f, sep=",", header=None) for f in all_rec]
df = pd.concat(dataframes, ignore_index=True)
df.columns = ['Month', 'DelayRate']

df['Month'] = df['Month'].astype(int)
df = df.sort_values('Month')
df['DelayRate_pct'] = df['DelayRate'] * 100

fig, ax = plt.subplots(figsize=(12,5))
ax.plot(df['Month'], df['DelayRate_pct'], marker='o', color='purple', linewidth=2)
ax.fill_between(df['Month'], df['DelayRate_pct'], alpha=0.2, color='purple')

for _, row in df.iterrows():
    ax.annotate(f"{row['DelayRate_pct']:.1f}%", 
                (row['Month'], row['DelayRate_pct']),
                textcoords="offset points", 
                xytext=(0,8), 
                ha='center', 
                fontsize=9)

ax.set_title("Ty Le Chuyen Bay Bi Tre Theo Thang")
ax.set_xlabel("Thang")
ax.set_ylabel("Ty le tre (%)")
ax.set_xticks(range(1,13))
plt.tight_layout()

plt.savefig('/home/hadoopuser/bai5_chart.png', dpi=150)
print("Da luu bieu do tai /home/hadoopuser/bai5_chart.png")