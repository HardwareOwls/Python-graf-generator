from pandas import DataFrame, read_csv

import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib

in_ = "2.csv"
out_ = "bar.png"

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

df = pd.read_csv(in_, names=['y'])
#print(df)
print(df['y'].max())
ax = df['y'].plot()
fig = ax.get_figure()
fig.savefig(out_)
