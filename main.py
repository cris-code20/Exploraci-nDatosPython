from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('avocado.csv')

# muesta las dimenciones
print(data.shape) 

# muestra los primeros 100 valores
print(data.head(101)) 

# muestra los ultimos 20 valores
print(data.tail(20)) 

# muestra el precio maximo y el minimo del aguacate ademas del promedio
print(data.describe())

# creando las graficas respectivas de el aguacate 

Albany = data[data['region'] == 'Albany']
West = data[data['region'] == 'West']
Detroit = data[data['region'] == 'Detroit']

x1 = plt.subplot()
Albany_grafica = Albany.plot(x='year', y='AveragePrice', kind='scatter', ax=x1, color ='red') 
West_grafica = West.plot(x='year', y='AveragePrice', kind='scatter', ax=x1,color ='blue')
Detroit_grafica = Detroit.plot(x='year', y='AveragePrice', kind='scatter', ax=x1, color ='green')
plt.show()