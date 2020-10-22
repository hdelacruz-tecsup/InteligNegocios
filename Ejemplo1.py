import pandas as pd
import matplotlib.pyplot as plt

archivo="WEO_Data.csv"
df=pd.read_csv(archivo,thousands=',',decimal='.')#para que acepte decimalkes
df.rename(columns={'Country':'Pais'},inplace=True)#para renombrar el nombre del Country
df.set_index('Pais',inplace=True)#para agregar indice al campo
tiempo=list(map(str,range(2008,2024)))#agregamos solo los campos de 2008 al 2024

#iniciamos una funcion
def grafico1_area():
    df.sort_values(by='2020', ascending=False)# seleccionamos solo del año 2020 y ordenandolo
    df_top5=df[tiempo].head(5)#solograficaremos los 5 primeros
    df_top5=df_top5.transpose()# invirtiendo los datros pero teniendo en la mismma variable
    print(df_top5.head())
    df_top5.plot(kind='area',alpha=0.50)
    plt.title('PBI por paises - Top 5')
    plt.ylabel('Millones $')
    plt.xlabel('Años')
    plt.show()
grafico1_area()





