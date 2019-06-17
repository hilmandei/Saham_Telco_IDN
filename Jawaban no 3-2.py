import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlalchemy

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


df1 = pd.read_csv(r'E:\A. Coding\Purwadhika\Ujian\2\Ujian_AnalyticsVisualization_JCDS04-master\Ujian_AnalyticsVisualization_JCDS04-master\dataSaham\EXCL.JK.csv', parse_dates=['Date'], index_col='Date')
df2 = pd.read_csv(r'E:\A. Coding\Purwadhika\Ujian\2\Ujian_AnalyticsVisualization_JCDS04-master\Ujian_AnalyticsVisualization_JCDS04-master\dataSaham\FREN.JK.csv', parse_dates=['Date'], index_col='Date')
df3 = pd.read_csv(r'E:\A. Coding\Purwadhika\Ujian\2\Ujian_AnalyticsVisualization_JCDS04-master\Ujian_AnalyticsVisualization_JCDS04-master\dataSaham\ISAT.JK.csv', parse_dates=['Date'], index_col='Date')
df4 = pd.read_csv(r'E:\A. Coding\Purwadhika\Ujian\2\Ujian_AnalyticsVisualization_JCDS04-master\Ujian_AnalyticsVisualization_JCDS04-master\dataSaham\TLKM.JK.csv', parse_dates=['Date'], index_col='Date')

print(type(df1.index[0]))
dft = pd.date_range(start='4/1/2019', end='4/30/2019')
print(dft)

plt.figure(figsize=(15, 8))
plt.title('Harga Historis Saham Provider Telco Indonesia (April 2019)', pad=30)
plt.style.use('ggplot')
plt.plot(df1['04-2019'].index, df1['04-2019']['Close'], label='PT XL Axiata Tbk')
plt.plot(df2['04-2019'].index, df2['04-2019']['Close'], label='PT Smartfren Telecom Tbk')
plt.plot(df3['04-2019'].index, df3['04-2019']['Close'], label='PT Indosat Tbk')
plt.plot(df4['04-2019'].index, df4['04-2019']['Close'], label='PT Telekomunikasi Indonesia')
plt.xticks(rotation=45)
plt.legend(loc='upper center', ncol=4, fontsize=8, bbox_to_anchor=(0.5, 1.05))
plt.xlabel('Tanggal')
plt.ylabel('Rupiah(IDR)')

plt.xticks(dft)

plt.grid(True)


plt.show()

