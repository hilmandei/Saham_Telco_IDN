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

dft = pd.date_range(start='3/15/2019', end='6/17/2019', freq='w')
print(dft)

plt.figure(figsize=(15, 8))

plt.title('Harga Historis Saham Provider Telco Indonesia', pad=30)
plt.style.use('ggplot')
plt.plot(df1.index, df1['Close'], label='PT XL Axiata Tbk')
plt.plot(df2.index, df2['Close'], label='PT Smartfren Telecom Tbk')
plt.plot(df3.index, df3['Close'], label='PT Indosat Tbk')
plt.plot(df4.index, df4['Close'], label='PT Telekomunikasi Indonesia')
plt.xticks(rotation=45)
plt.legend(loc='upper center', ncol=4, fontsize=8, bbox_to_anchor=(0.5, 1.05))
plt.xlabel('Tanggal')
plt.ylabel('Rupiah(IDR)')

plt.xticks(dft)

plt.grid(True)


plt.show()

