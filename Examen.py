import pandas as pd

archivo = pd.read_csv("medallero_Panamericanos_Lima2019.csv")
df=pd.DataFrame(archivo)

def cal_media():
    print("====================================")
    print("calcular la media de la columna Oro")
    media=df.Oro.mean()
    print(media)
    print("------------------------------------")
    print("Calcular la media de la columna Plata")
    media=df.Plata.mean()
    print(media)
    print("\n")
cal_media()


def cal_mediana():
    print("======================================")
    print("Calcular la mediana de la columna Oro")
    mediana=df.Oro.median()
    print(mediana)
    print("--------------------------------------")
    print("Calcular la mediana de la columna Plata")
    mediana=df.Plata.median()
    print(mediana)
    print("\n")
cal_mediana()


def cal_moda():
    print("====================================")
    print("calcular la moda de la columna Oro")
    moda=df.Oro.mode()
    print(moda)
    print("------------------------------------")
    print("Calcular la moda de la columna Plata")
    moda=df.Plata.mode()
    print(moda)
cal_moda()
