'''
15.08.2020 - Primeira versão
Autor: Iago Leonardo Alves de Oliveira
----------------------------------------
Criação de um jogo de carros com PyGame
Com interface grafica e recebendo comandos do teclado
----------------------------------------
'''
#Importando as bibliotecas
import pygame #pip install pygame
import random
import os

#Inicializa o PyGame
pygame.init()

#Recebe o caminho em que o script está sendo executado
caminhoAtual = os.path.abspath(os.path.dirname(__file__))

#Definindo o tamanho da janela
janela = pygame.display.set_mode((1000, 650))
#Definindo o nome da Janela
pygame.display.set_caption("Corrida")

janelaAberta = True

#Painel de contagem de pontos
#Fonte
fonte = pygame.font.SysFont('arialblack', 15)
#Texto / Cor Letra/ Cor Fundo
texto = fonte.render("Pontos: ",True, (255, 255, 255), (0, 0, 0))
#Posição
posi_texto = texto.get_rect()
posi_texto.center = (40, 20)

#Cria um timer para calcular a pontuação
timer = 0
pontos = 0

#Variáveis que armazenam posições e velocidade do jogador
x = 465
y = 440
velocidade = 10

#Variáveis que armazenam as ruas dos NPCs
#Posição X das ruas = 180, 412, 640
rua_caminho = 180
rua_policia = 180 
rua_carBranco = 412
rua_taxi = 640
rua_policia2 = 640

#Varoáveis que armazenam as posições Y dos NPCs e Fundo
npc_y = [-500, -700, -950, -1250, -1600]
fundo_y = -900

#Sorteia uma posição inicial para cada NPC
policia_y = random.choice(npc_y)
policia_x = rua_policia
carBranco_y = random.choice(npc_y)
carBranco_x = rua_carBranco
taxi_y = random.choice(npc_y)
taxi_x = rua_taxi
caminho_y = random.choice(npc_y)
caminho_x = rua_caminho
policia2_y = random.choice(npc_y)
policia2_x = rua_policia2

#Variáveis que armazenam o fundo e os carros
fundo = pygame.image.load(caminhoAtual + '/fundos/rua.jpg')
carro = pygame.image.load(caminhoAtual + '/carros/carro_amarelo.png')
carroDir = pygame.image.load(caminhoAtual + '/carros/carro_amarelo-dir.png')
carroEsq = pygame.image.load(caminhoAtual + '/carros/carro_amarelo-esq.png')
#NPCs
taxi = pygame.image.load(caminhoAtual + '/carros/taxi.png')
policia = pygame.image.load(caminhoAtual + '/carros/policia.png')
carBranco = pygame.image.load(caminhoAtual + '/carros/carro_branco.png')
caminhonete = pygame.image.load(caminhoAtual + '/carros/caminhonete.png')
policia2 = pygame.image.load(caminhoAtual + '/carros/policia.png')

#Enquanto a janela estiver aberta
while janelaAberta:
    #Define um delay para atualização da tela
    pygame.time.delay(50)

    #Velocidade dos NPCs
    npc_velocidade = 15
    policia_velocidade = 2

    #Velocidade dos fundos
    fundo_velocidade = 30

    #Definindo os eventos
    for event in pygame.event.get():
        #Se o tipo do evento for SAIR / Usuário clicar no X
        if event.type == pygame.QUIT:
            #retorna Falso para sair do loop While e fechar a janela
            janelaAberta = False

    ###################################
    #Recebe o valor da tecla pressionada
    comando = pygame.key.get_pressed()

    #Se a tecla pressionada for a 'seta para cima'
    if comando[pygame.K_UP] and y > 10:
        #A posição Y diminui valor da velocidade (move a imagem para cima)
        y -= velocidade - 6
        #Também aumenta em 50% a velocidade do fundo e NPCs /Simula que o jogador está mais rápido
        #Diminui em 1 a velocidade da policia, para simular que ela está correndo mais
        policia_velocidade -= 1
        npc_velocidade += (npc_velocidade/2)
        fundo_velocidade += (fundo_velocidade/2)

    #Se a tecla pressionada for a 'seta para baixo' e o carro ainda estiver na rua
    if comando[pygame.K_DOWN] and y < 460:
        #A posição Y aumenta valor da velocidade (move a imagem para baixo)
        y += velocidade - 9
        #Também diminue metade da velocidade do fundo e NPCs /Simula que o jogador está mais lento
        npc_velocidade = (npc_velocidade/2)
        fundo_velocidade = (fundo_velocidade/1.5)
    
    #Se a tecla pressionada for a 'seta para baixo' e o carro estiver no final da rua
    if comando[pygame.K_DOWN] and y >= 460:
        #diminue metade da velocidade do fundo e NPCs /Simula que o jogador está mais lento
        npc_velocidade = (npc_velocidade/2)
        fundo_velocidade = (fundo_velocidade/1.5)

    #Se a tecla pressionada for a 'seta para direita' e o carro estiver dentro da rua
    if comando[pygame.K_RIGHT] and x < 895:
        #A posição X aumenta valor da velocidade (move a imagem para direita)
        x += velocidade

        carro = carroDir

    #Se a tecla pressionada for a 'seta para esquerda' e o carro estiver dentro da rua
    if comando[pygame.K_LEFT] and x > 125:
        #A posição X diminui valor da velocidade (move a imagem para esquerda)
        x -= velocidade
        carro = carroEsq

    #Se a tecla ESPAÇO for pressionada e o jogador tiver perdido
    if comando[pygame.K_SPACE] and y == 5000:
        #Retoma ele de volta
        y = 440
        

    ##################################
    #Conta o tempo para calcular a pontuação
    if timer < 20:
        timer += 1

    else:
        pontos += 0.4
        pontos = round(pontos, 2)
        texto = fonte.render("Pontos: {}".format(str(pontos)),True, (255, 255, 255), (0, 0, 0))



    ##################################
    #Traz o efeito de 'esteira' para o fundo
    if fundo_y >= 0:
        #Traz ele de volta para cima
        fundo_y = -1800

    ##################################
    #Se os NPCs sairem da tela, os trazem de volta
    if policia_y >= 690:
        #Coloca a policia na rua certa
        policia_x = rua_policia
        #Traz ele de volta para cima /Sorteia posição Y
        policia_y = random.choice(npc_y)

    if policia2_y >= 690:
        #Coloca a policia na rua certa
        policia2_x = rua_policia2
        #Traz ele de volta para cima /Sorteia posição Y
        policia2_y = random.choice(npc_y)

    if taxi_y >= 690:
        #Traz ele de volta para cima /Sorteia posição Y
        taxi_y = random.choice(npc_y)

    if caminho_y >= 690:
        #Traz ele de volta para cima /Sorteia posição Y
        caminho_y = random.choice(npc_y)

    if carBranco_y >= 690:
        #Traz ele de volta para cima /Sorteia posição Y
        carBranco_y = random.choice(npc_y)


    #COLISÃO X80 Y220
    #Colisão direita
    if ((x + 85 >= taxi_x and y - 225 <= taxi_y) and (x + 85 >= taxi_x and y + 225 >= taxi_y)):
        y = 5000

    #Colisão direita
    if ((x + 85 >= policia2_x and y - 225 <= policia2_y) and (x + 85 >= policia2_x and y + 225 >= policia2_y)):
        y = 5000

    #Colisão esquerda
    if ((x - 85 <= policia_x and y - 225 <= policia_y)and (x - 85 <= policia_x and y + 225 >= policia_y)):
        y = 5000

    #Colisão esquerda
    if ((x - 85 <= caminho_x and y - 225 <= caminho_y) and (x - 85 <= caminho_x and y + 225 >= caminho_y)):
        y = 5000

    #Colisão central
    if ((x + 85 >= carBranco_x and y - 225 <= carBranco_y) and (x - 85 <= carBranco_x and y + 225 >= carBranco_y)):
        y = 5000

    #Colisão central
    if ((x + 85 >= policia2_x and y - 225 <= policia2_y) and (x - 85 <= policia2_x and y + 225 >= policia2_y)):
        y = 5000

    #Colisão central
    if ((x + 85 >= policia_x and y - 225 <= policia_y) and (x - 85 <= policia_x and y + 225 >= policia_y)):
        y = 5000

    #################################
    #Desvio da Policia, para não bater
    #Se a policia for bater na caminhonete, vira para a direita
    if ((policia_x - 85 <= caminho_x and policia_y - 225 <= caminho_y) and (policia_x - 85 <= caminho_x and policia2_y + 225 >= caminho_y)):
        policia_x = 305

    if ((policia2_x + 85 >= taxi_x and policia2_y - 225 <= taxi_y) and (policia2_x - 85 <= taxi_x and policia2_y + 225 >= taxi_y)):
        policia2_x = 525
    

    #Aumenta o (valor da velocidade) da posição Y dos NPCs/ Isso faz com que ele se mova para baixo
    policia_y += policia_velocidade
    policia2_y += policia_velocidade
    carBranco_y += npc_velocidade
    taxi_y += npc_velocidade
    caminho_y += npc_velocidade

    #Aumenta o (valor da velocidade) da posição Y do Fundo/ Isso faz com que ele se mova para baixo
    fundo_y += fundo_velocidade

    #Coloca o fundo da tela
    janela.blit(fundo, (0, fundo_y))

    #exibe os carros na tela
    janela.blit(carro, (x, y))
    janela.blit(policia, (policia_x, policia_y))
    janela.blit(policia2, (policia2_x, policia2_y))
    janela.blit(caminhonete, (caminho_x, caminho_y))
    janela.blit(taxi, (taxi_x, taxi_y))
    janela.blit(carBranco, (carBranco_x, carBranco_y))

    carro = pygame.image.load(caminhoAtual + '/carros/carro_amarelo.png')

    #exibe a pontuação
    janela.blit(texto, posi_texto)

    #Atualiza a tela
    pygame.display.update()

pygame.quit()