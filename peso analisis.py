import pandas as pd
df=pd.read_csv('peso_estatura_genero.csv')
print('Cantidad de renglones ',len(df.index))
print(df.describe())