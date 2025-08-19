import pygame

#iniciar game
pygame.init()

resolucao_tela = (800,800)
tela = pygame.display.set_mode(resolucao_tela)
pygame.display.set_caption("Bloc_Destructor")

tamanho_bola = 15
bola = pygame.Rect(100, 500, tamanho_bola, tamanho_bola)
tamanho_jogador = 100
jogador = pygame.Rect(0, 750, tamanho_jogador,tamanho_bola)


qtde_bloco = 8
qtde_linha = 5
totqtde_Blocos = qtde_bloco * qtde_linha

def criar_blocos(qtde_linha, qtde_bloco):
    altura_tela = resolucao_tela[1]
    largura_tela = resolucao_tela[0]
    distancia_entre_blocos = 5
    largura_bloco = largura_tela / 8 - distancia_entre_blocos
    altura_bloco = 15
    distancia_entre_linhas = altura_bloco + 10


    blocos = []
    #Criar blocos
    for j in  range(qtde_bloco):
        for i in range(qtde_linha):
        #Criar bloco
          bloco = pygame.Rect(i * (largura_bloco + distancia_entre_blocos), j * distancia_entre_linhas , largura_bloco, altura_bloco)
        #Adicionar bloco
          blocos.append(bloco)

   
    return  blocos

# Tipos de cores
cores = {
    "branco": (255, 255, 255),
    "preto": (0, 0, 0),
    "azul": (0, 0, 255),
    "amarelo": (255, 255, 0),
    "verde": (0, 255, 0)

}

fim_jogo = False
pontuacao = 0
movimento_bola = [1, -1]


#Funções do game

def movimentar_jogador(evento):
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_RIGHT:
            if (jogador.x + tamanho_jogador) < (resolucao_tela[0]): 
                jogador.x = jogador.x + 2
        if evento.key == pygame.K_LEFT:
            if jogador.x > 0:
                 jogador.x = jogador.x - 2




def movimentar_bola(bola):
    movimento = movimento_bola
    bola.x = bola.x + movimento[0]
    bola.y = bola.y + movimento[1]

    if bola.x <= 0:
        movimento[0] = - movimento[0]
    if bola.y <= 0:
        movimento[1] = - movimento[1]
    if bola.x + tamanho_bola >= resolucao_tela[0]:
        movimento[0] = - movimento[0]
    if bola.y + tamanho_bola >= resolucao_tela[1]:
        movimento = None
    if jogador.collidepoint(bola.x, bola.y):
        movimento[1] = - movimento[1]
    for bloco in blocos:
        if bloco.collidepoint(bola.x, bola.y):
            blocos.remove(bloco) #remover blocos
            movimento[1] = - movimento[1]
    return movimento
def atualizar_pontuacao(pontuacao):
    fonte = pygame.font.Font(None, 35)
    texto = fonte.render(f"PontuaÇâo: {pontuacao}", 1, cores["amarelo"])
    tela.blit(texto, (0, 700))
    if pontuacao >= totqtde_Blocos:
        return True
    else:
        return False

def game_over(over):
    fonte = pygame.font.Font(none, 89)
    texto = fonte.render(f"FIM DE JOGO")
    tela.blit(texto, (399, 399))   
    if evento.type == pygame.QUIT:
         return over
    else:
        return False


#Desenhar elementos da tela
def desenhar_in_jogo():
    tela.fill(cores["preto"])
    pygame.draw.rect(tela, cores["azul"], jogador)
    pygame.draw.rect(tela, cores["branco"], bola)

def desenhar_blocos(blocos):
    for bloco in blocos:
        pygame.draw.rect(tela, cores["verde"], bloco)


blocos = criar_blocos(qtde_bloco, qtde_linha)

#Criar loop
while not fim_jogo:
    desenhar_in_jogo()
    desenhar_blocos(blocos)
    game_over= atualizar_pontuacao(totqtde_Blocos - len(blocos))    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_over = True
    movimentar_jogador(evento)
    movimento_bola = movimentar_bola(bola)
    if not movimento_bola:
      game_over = True
    pygame.time.wait(1)
    pygame.display.flip()


pygame.quit()