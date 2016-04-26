# Importerer alle de libs der skal bruges og maaske lidt mere
from pandas import DataFrame, read_csv
from matplotlib import cm
import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib
import glob
import os
import random

# Skriver lidt ting ud om versioner
print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

# Funktion, som kan generere en vaerdi mellem 0 og 255 til random farver
r = lambda: random.randint(0,255)
cmap = cm.get_cmap('jet')

# Finder alle filerne og laver en figur af hver enkelt, som gemmes som billede
path = './'
files = []
all_files = glob.glob(path + "*.csv")
for file in all_files:
	vars = file.split("+")
	files.append([file,vars[1].replace(".csv","")])
	df = pd.read_csv(file, names=[vars[1].replace(".csv","")], header=None)
	ax = df.plot()
	fig = ax.get_figure()
	fig.savefig(file.replace(".csv",'.png'))

# Laver en liste med alle de fundne kurver
ax = None
frame = pd.DataFrame()
list_ = []
for file in files:
	df = pd.read_csv(file[0], names=[file[1]], header=None, index_col=None)
	list_.append(df)

# Gemmer den samlede fil
frame = pd.concat(list_)
ax = frame.plot(cmap=cmap)
ax.set_xlabel('Sample')
ax.set_ylabel('Latency [ms]')
fig = ax.get_figure()
fig.savefig('foo.png')
