import pandas as pd
import client as c
# Crear un DataFrame de ejemplo

data = c.Data_Frame

df = pd.DataFrame(data)

# Guardar el DataFrame como un archivo CSV
df.to_csv("BTCUSDT.csv", index=False)