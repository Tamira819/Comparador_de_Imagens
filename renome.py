import os
import pandas as pd

# Caminhos
pasta_imagens = r"C:/Users/TamiradeSenaAbo-gane//LORE CONFECCOES LTDA/Analista ADM - General/imagem/Fotos Originais"
arquivo_excel = r"C:/Users/TamiradeSenaAbo-gane/LORE CONFECCOES LTDA/Analista ADM - General/imagem/nomes_fotos.xlsx"

# Ler o arquivo Excel
df = pd.read_excel(arquivo_excel, sheet_name='Planilha1')

# Iterar sobre as linhas do DataFrame
for index, row in df.iterrows():
    nome_antigo = row['A']  # Nome antigo (coluna A)
    nome_novo_B = row['C']  # Novo nome parte B (coluna B)
    nome_novo_C = row.get('C.1', '')  # Novo nome parte C (coluna C), se existir
    
    # Se a coluna C não tiver valor, usar apenas o valor da coluna B
    if pd.isna(nome_novo_C):
        novo_nome = nome_novo_B.replace('.jpg', '')  # Remover a extensão
    else:
        novo_nome = f"{nome_novo_B.replace('.jpg', '')} {nome_novo_C.replace('.jpg', '')}"  # Concatenar B e C
    
    # Caminhos completos dos arquivos
    caminho_antigo = os.path.join(pasta_imagens, nome_antigo)
    caminho_novo = os.path.join(pasta_imagens, f"{novo_nome}.jpg")  # Adicionar a extensão .jpg ao novo nome
    
    # Renomear o arquivo
    if os.path.exists(caminho_antigo):
        os.rename(caminho_antigo, caminho_novo)
        print(f"Arquivo renomeado: {nome_antigo} -> {novo_nome}.jpg")
    else:
        print(f"Arquivo {nome_antigo} não encontrado.")
