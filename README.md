Este código compara imagens e identifica as melhores correspondências.

Ele serve para ajudar a renomear as imagens de acordo com a referência da peça no ERP da fábrica, de modo que a equipe de Marketing possa buscar a foto pela referência da peça.

~ Tratam-se de imagens da coleção de roupas, por isso são frente e costas da mesma roupa, uma mesma estampa que aparece em diferentes peças, a mesma modelo aparece em diferentes fotos, etc.
No entanto, as imagens comparadas não são iguais. Uma pasta contém fotos 'croppadas', ou seja, já editadas pela equipe de marketing. Enquanto que a outra pasta contém as fotos originais, maiores e com maior resolução de imagem.

É um código simples e leve, que coloca a condição de que, uma vez encontrada a correspondência para uma imagem, ela não volta a ser comparada com as imagens restantes.
Dessa forma foi possível reduzir a quantidade de comparações e consequentemente o tempo de execução do código.
Ainda assim, ele funciona melhor com pequenos grupos de imagens, em torno de 50 imagens por vez.

Sendo a 1a versão do código, eu preferi separar a comparação de imagens e a parte de renomear.
O código compara e salva as correspondências em uma planilha excel, assim, a equipe pode conferir e corrigir caso seja necessário.
A acurácia é de mais de 90%.

