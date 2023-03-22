import pandas as pd
import pandas as pd



# Creamos un dataframe de ejemplo
data = {'Columna1': [1, 2, 3, 4, 4, 5, 6],
        'Columna2': ['A', 'B', 'C', 'D', 'E', 'F', 'G']}
df = pd.DataFrame(data)

# Eliminar duplicados de la columna1
df = df.drop_duplicates(subset=['Columna1'])

# Ordenar por columna2
df = df.sort_values(by=['Columna2'])

# Filtrar datos de columna1 mayores que 3
df = df[df['Columna1'] > 3]

# Eliminar datos de columna1 iguales a 5
df = df[df['Columna1'] != 5]

print(df)
