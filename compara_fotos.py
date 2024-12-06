import cv2
import os
import pandas as pd

# Caminhos para as pastas de imagens
pasta_primeiro = r"C:/Users/GuilhermedeAlencarSi/LORE CONFECCOES LTDA/Analista ADM - General/imagem/teste_primeiro"
pasta_drop_1 = r"C:/Users/GuilhermedeAlencarSi/LORE CONFECCOES LTDA/Analista ADM - General/imagem/teste_drop_1"
output_excel = r"C:/Users/GuilhermedeAlencarSi/LORE CONFECCOES LTDA/Analista ADM - General/imagem/correspondencias_imagens.xlsx"

# Função para listar as imagens de uma pasta e retornar uma lista com os caminhos completos
def listar_imagens(pasta):
    return [os.path.join(pasta, f) for f in sorted(os.listdir(pasta)) if f.endswith(('.jpg', '.jpeg', '.png'))]

# Função para comparar imagens usando ORB
def comparar_imagens_orb(img1_path, img2_path):
    # Carregar as imagens
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

    if img1 is None or img2 is None:
        print(f"Erro ao carregar imagem: {img1_path}, {img2_path}")
        return 1000  # Retorna um valor alto para indicar que não houve correspondência

    # Inicializa o detector ORB
    orb = cv2.ORB_create()

    # Detectar keypoints e calcular os descritores
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    if des1 is None or des2 is None:
        return 1000  # Valor alto para indicar ausência de correspondência

    # Criar o objeto BFMatcher para correspondência de características
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Encontra as correspondências
    matches = bf.match(des1, des2)

    # Ordena as correspondências pela distância (quanto menor, melhor)
    matches = sorted(matches, key=lambda x: x.distance)

    # Retorna a pontuação média das melhores correspondências
    if len(matches) > 10:  # Considera apenas as 10 melhores correspondências
        melhores_matches = matches[:10]
        score = sum([m.distance for m in melhores_matches]) / len(melhores_matches)
        return score
    else:
        return 1000  # Um valor alto indicando que as imagens não são muito parecidas

# Função para encontrar correspondências entre imagens da pasta drop_1 e pasta Primeiro
def encontrar_correspondencias(caminhos_primeiro, caminhos_drop_1, limite=60):
    correspondencias = []

    # Criação de uma cópia mutável da lista de imagens "drop_1"
    caminhos_drop_1_restantes = caminhos_drop_1.copy()

    # Iterar sobre todas as imagens da pasta "Primeiro"
    for caminho_primeiro in caminhos_primeiro:
        melhor_correspondencia = None
        melhor_score = 1000  # Inicializamos com um valor alto

        # Iterar sobre todas as imagens restantes da pasta "drop_1"
        for caminho_drop in caminhos_drop_1_restantes:
            score = comparar_imagens_orb(caminho_primeiro, caminho_drop)

            # Se a pontuação for melhor (menor), atualizamos a melhor correspondência
            if score < melhor_score and score < limite:
                melhor_score = score
                melhor_correspondencia = caminho_drop

        if melhor_correspondencia:
            # Adiciona a correspondência e remove a imagem correspondente da lista de imagens restantes
            correspondencias.append({
                "Imagem Primeiro": os.path.basename(caminho_primeiro),
                "Imagem Drop_1": os.path.basename(melhor_correspondencia)                
            })
            # Remove a imagem da lista para não ser comparada novamente
            caminhos_drop_1_restantes.remove(melhor_correspondencia)
            print(f"Match encontrado: {os.path.basename(caminho_primeiro)} -> {os.path.basename(melhor_correspondencia)}")
        else:
            correspondencias.append({
                "Imagem Primeiro": os.path.basename(caminho_primeiro),
                "Imagem Drop_1": "Nenhuma correspondência",
                "Pontuação de Correspondência": "N/A"
            })

    return correspondencias

# Listar imagens das pastas
caminhos_primeiro = listar_imagens(pasta_primeiro)
caminhos_drop_1 = listar_imagens(pasta_drop_1)

# Encontrar as correspondências
correspondencias = encontrar_correspondencias(caminhos_primeiro, caminhos_drop_1)

# Criar um DataFrame com as correspondências e salvar no Excel
df = pd.DataFrame(correspondencias)
df.to_excel(output_excel, index=False)
print(f"Correspondências salvas em {output_excel}")
