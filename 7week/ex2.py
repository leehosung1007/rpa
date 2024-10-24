import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('2024_seoul_data.csv', encoding = 'utf-8')
df2 = df.fillna(method='ffill')
df2.info()

df2.rename(columns={'일강수량':'rain_amount'}, inplace=True)
df2.rename(columns={'일시':'date'}, inplace=True)
df2.head(3)

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

plt.title('서울시 2024년도 여름 강수량 변화')
plt.plot(df2['date'], df2['rain_amount'], label = '강수량', c = 'r')
plt.xticks()
plt.xlabel('')
plt.ylabel('강수량')
plt.legend()
plt.show()
