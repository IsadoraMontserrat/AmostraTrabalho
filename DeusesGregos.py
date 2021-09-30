#Deuses gregos (Trabalho)

import pandas as pd
import numpy as np

#Lê e mostra toda a base de dados
base = pd.read_csv('greek_gods.csv')
base

#Tamanho da base de dados
base.shape

#Selecionar uma quantidade específica para a amostra
np.random.seed(1604)
amostra = np.random.choice(a = [0,1], size = 445, replace=True, p = [0.75,0.25])
print(len(amostra))
print(len(amostra[amostra==0]))
print(len(amostra[amostra==1]))

#Mostra todos os elementos que foram selecionados para a amostra final, juntamente com todos os dados amostra_final = base.loc[amostra==1]
print(amostra_final.shape)
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(amostra_final)

#Mostra apenas a categoria de cada amostra final
amostra_final['main-type'].value_counts()
