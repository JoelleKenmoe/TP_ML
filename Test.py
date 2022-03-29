
from datetime import date
import numpy as np
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf
from pandas import DataFrame
from pandas import concat
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
import matplotlib.pyplot as plt

data = pd.read_csv(r/home/bb-joelle/Tp 3125/.csv') #, index_col=0, parse_dates=True)
data.columns=['a','b']
data.set_index('a', inplace=True)
#print(data.tail())

# Nuage de points
#values = DataFrame(data['b'])
#lags=8
#columns = [values]
#for i in range(1,(lags + 1)):
#	columns.append(values.shift(i))
#dataframe = concat(columns, axis=1)
#columns = ['t']
#for i in range(1,(lags + 1)):
#	columns.append('t+' + str(i))
#dataframe.columns = columns
#print(dataframe.columns)
#pyplot.figure(1)
#for i in range(1,(lags + 1)):
#	ax = pyplot.subplot(240 + i)
#	ax.set_title('t vs t+' + str(i))
#	pyplot.scatter(x=dataframe['t'].values, y=dataframe['t+'+str(i)].values)
#pyplot.show()

#representation de la serie
#data['b'].plot()
#plt.show()

#courbe d'autocorrelation
#print(data.isna().sum())
plot_acf(data['b'], lags=50)
plt.title('autocorrelation de l evolution de la consommation de biere')
plt.show()

# decomposition de la
#result= seasonal_decompose(data['Airpass'], model='additive', period=12)
#result.plot()
#plt.show()