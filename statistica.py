from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('experiment.csv', sep=',')
print(df)

df1 = pd.DataFrame(data={
    'df': df['numbers'],
})

df1.plot.kde()
plt.show()

d = df1['df']

print(stats.kstest(d, 'norm', (d.mean(), d.std()), N=len(d)))