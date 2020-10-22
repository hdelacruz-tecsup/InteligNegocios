import xlrd # para leer el archivo de excel
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_excel('BI_Clientes.xlsx')
print("\n")
grupo2=data.groupby('Gender')['Gender'].count()
print(grupo2)
print("\n")
#*************************
grupo2.plot(kind='barh')
plt.show()

grupo3=data.groupby('Gender')['YearlyIncome'].sum()
print(grupo3)
print("\n")
#*************************
grupo3.plot(kind='bar')
plt.show()


grupo4=data.groupby('Gender')['YearlyIncome'].mean()
print(grupo4)
print("\n")
#*************************
grupo4.plot(kind='pie')
plt.show()

