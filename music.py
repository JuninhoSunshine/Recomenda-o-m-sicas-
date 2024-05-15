musicas = [
    ("Música 1", "Rock"),
    ("Música 2", "Pop"),
    ("Música 3", "Jazz"),
    ("Música 4", "Funk"),
    ("Música 5", "Rap"),
]  

# Histórico de músicas ouvidas pelo usúario
historico_usuario =["Rock", "Pop", "Jazz", "Funk", "Rap"]


# Função para recomendar músicas
def recomendar_musica(historico):
    # Contar a frequência de cada gênero no histórico
    Frequencia = {}
    for genero in historico:    
        if genero in Frequencia:
            Frequencia [genero] += 1
        else:
            Frequencia [genero] = 1

 # Encontrar o gênero mais frequente
    genero_mais_frequente = max(Frequencia, key=Frequencia.get)  

  # Recomendar músicas desse gênero
    recomendacoes = []
    for titulo, genero in musicas:
        if genero == genero_mais_frequente:
            recomendacoes.append(titulo) 
    return recomendacoes 


#Obter recomendações para o usuário
recomendacoes_usuario =recomendar_musica (historico_usuario)
print("Músicas recomendadas:", recomendacoes_usuario) 
