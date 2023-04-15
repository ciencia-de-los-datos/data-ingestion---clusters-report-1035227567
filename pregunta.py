"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

   df=pd.read_fwf('clusters_report.txt',widths=[9,16,16,77])
   df=df.fillna(method='ffill')
   df=df.groupby(df.columna[0]).agg({df.columna[1]: 'first', df.columna[2]: 'first', df.columna[3]: lambda x: ' '.join(x)}).reset_index()
   df=df.rename(columna={'Cluster':'cluster','Cantidad de':'cantidad_palabras_clave','Porcentaje de':'porcentaje_de_palabras_clave','Principales palabras clave':'principales_palabras_clave'})
   df.drop(0,axis=0,inplace=True)
    
   df['cluster'] = df['cluster'].astype(int)
   df = df.sort_values('cluster')
   df['cantidad_palabras_clave'] = df['cantidad_palabras_clave'].astype(int)

   df['porcentaje_palabras_clave']=df['porcentaje_palabras_clave'].str.replace('%', '', regex=True)
   df['porcentaje_palabras_clave'] = df['porcentaje_palabras_clave'].str.replace(',', '.', regex=True).astype(float)

   df['principal_palabras_clave']=df['principal_palabras_clave'].str.replace('\s+', ' ', regex=True)
   df['principal_palabras_clave']=df['principal_palabras_clave'].str.replace(',+', ',', regex=True)
   df['principal_palabras_clave'] = df['principal_palabras_clave'].apply(lambda x: x.replace('.', ''))
 
   return df
