import pandas as pd

# sheet_name = 1 significa que coge los datos de la segunda hoja
df = pd.read_excel('G89.2023.T15.EG3.xlsx', sheet_name=1)

for index, row in df.iterrows():
    file_name = row['FILE PATH']
    file_content = row['FILE CONTENT']

    with open(file_name, 'w') as f:
        f.write(str(file_content))
