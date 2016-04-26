# Importerer alle de libs der skal bruges og maaske lidt mere
from pandas import DataFrame, read_csv

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

# Laver en figur med alle de fundne kurver
ax = None
for file in files:
	df = pd.read_csv(file[0], names=[file[1]], header=None)
	c = '#%02x%02x%02x' % (r(),r(),r())
	ax = df.plot(color=c, ax=ax)

# Gemmer den samlede fil
fig = ax.get_figure()
fig.savefig('foobar.png')
