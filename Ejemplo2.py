import xlrd # para leer el archivo de excel
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_excel('BI_Clientes.xlsx')
grupo1=data.groupby('SpanishEducation')#agrupar los datos de un grupo mucho consumo
print(grupo1.describe())
print("\n")
grupo2=data.groupby('SpanishEducation').count()
print(grupo2)
print("\n")
grupo3=data.groupby('SpanishEducation')['SpanishEducation'].count()# solo por la columna especificada
print(grupo3)
print("\n")
grupo4=data.groupby('SpanishEducation')['YearlyIncome'].sum()#suma
print(grupo4)
print("\n")
grupo5=data.groupby('SpanishEducation')['YearlyIncome'].mean()#media
print(grupo5)
#Graficas
#Grafica del grupo 3 en modo de barra
grupo3.plot(kind='bar')
plt.show()

#Grafica del grupo 3 en modo de barra
grupo4.plot(kind='pie')
plt.show()

#Grafica del grupo 3 en modo de barra
grupo5.plot(kind='barh')
plt.show()










