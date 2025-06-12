print("Hello, World!")

import re

def converter_data_para_brasileiro(data_iso):
    # Expressão regular para capturar as partes da data no formato americano
    pattern = r'(\d{4})-(\d{2})-(\d{2})'
    
    # Utilizando re.sub para substituir e reorganizar os grupos capturados
    data_brasileira = re.sub(pattern, r'\3/\2/\1', data_iso)
    
    return data_brasileira

# Exemplo de teste com algumas datas
datas_teste = [
    "2025-02-07",
    "2024-12-25",
    "2023-07-14",
    "2022-01-01",
    "2021-09-03"
]

# Itera sobre as datas de teste e imprime o resultado da conversão
for data in datas_teste:
    print(f"Data original: {data} -> Data convertida: {converter_data_para_brasileiro(data)}")

