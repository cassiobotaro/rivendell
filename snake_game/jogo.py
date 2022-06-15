import pygame
import sys
from random import randint

pygame.init()

largura = 640
altura = 480
centro_da_tela = largura // 2, altura // 2

x_cobra, y_cobra = centro_da_tela

x_maçã = randint(40, 600)
y_maçã = randint(50, 430)

velocidade = 10
x_controle = velocidade
y_controle = 0


branco = (255, 255, 255)
verde = (0, 255, 0)
vermelho = (255, 0, 0)
preto = (0, 0, 0)

pontos = 0
fonte = pygame.font.SysFont("arial", 20, bold=True, italic=True)

comprimento_maximo_cobra = 5
está_morto = False
já_pausou = False

pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.load("backgroundmusic.ogg")
pygame.mixer.music.play(-1)

barulho_colisão = pygame.mixer.Sound("smw_coin.wav")

lista_cobra = []



tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo")
relogio = pygame.time.Clock()

def aumenta_cobra(lista_cobra):
    for x, y in lista_cobra:
        pygame.draw.rect(tela, verde, (x, y, 20, 20))

def reiniciar_jogo():
    global pontos, comprimento_maximo_cobra, x_cobra, y_cobra, lista_cobra, lista_cabeça, x_maçã, y_maçã, está_morto
    pontos = 0
    comprimento_maximo_cobra = 5
    x_cobra, y_cobra = centro_da_tela
    lista_cobra = []
    lista_cabeça = []
    x_maçã = randint(40, 600)
    y_maçã = randint(50, 430)
    está_morto = False

while True:
    relogio.tick(20)
    tela.fill(branco)
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, preto)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and y_controle != velocidade:
                y_controle = -velocidade
                x_controle = 0
            if evento.key == pygame.K_DOWN and y_controle != -velocidade:
                y_controle = velocidade
                x_controle = 0
            if evento.key == pygame.K_LEFT and x_controle != velocidade:
                x_controle = -velocidade
                y_controle = 0
            if evento.key == pygame.K_RIGHT and x_controle != -velocidade:
                x_controle = velocidade
                y_controle = 0
    
    x_cobra += x_controle
    y_cobra += y_controle

    cobra = pygame.draw.rect(tela, verde, (x_cobra, y_cobra, 20, 20))
    maçã = pygame.draw.rect(tela, vermelho, (x_maçã, y_maçã, 20, 20))

    if cobra.colliderect(maçã):
        x_maçã = randint(40, 600)
        y_maçã = randint(50, 430)
        pontos += 1
        barulho_colisão.play()
        comprimento_maximo_cobra += 1
    
    lista_cabeça = []
    lista_cabeça.append(x_cobra)
    lista_cabeça.append(y_cobra)

    
    lista_cobra.append(lista_cabeça)

    if lista_cabeça in lista_cobra[:-1]:
        fonte2 = pygame.font.SysFont("arial", 20, bold=True, italic=True)
        mensagem = "Fim do Jogo! Pressione a tecla R para jogar novamente"
        texto_formatado = fonte2.render(mensagem, True, preto)
        retângulo_texto = texto_formatado.get_rect()

        está_morto = True
        while está_morto:
            tela.fill(branco)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:
                        reiniciar_jogo()
            retângulo_texto.center = centro_da_tela
            tela.blit(texto_formatado, retângulo_texto)
            pygame.display.update()
    
    if pontos == 5 and not já_pausou:
        fonte2 = pygame.font.SysFont("arial", 20, bold=True, italic=True)
        mensagem = "Você está indo bem!"
        instrução = "Aperte R para continuar passando o tempo"
        texto_formatado = fonte2.render(mensagem, True, vermelho)
        texto_formatado2 = fonte2.render(instrução, True, preto)
        retângulo_mensagem = texto_formatado.get_rect()
        retângulo_instrução = texto_formatado2.get_rect()

        está_morto = True
        while está_morto:
            tela.fill(branco)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:
                        reiniciar_jogo()
            retângulo_mensagem.center = (largura // 2, altura // 2)
            retângulo_instrução.center = (largura // 2, altura // 2 + retângulo_mensagem.height + 10)
            tela.blit(texto_formatado, retângulo_texto)
            tela.blit(texto_formatado2, retângulo_instrução)
            pygame.display.update()
        já_pausou = True

    if x_cobra > largura:
        x_cobra = 0
    elif x_cobra < 0:
        x_cobra = largura
    elif y_cobra < 0:
        y_cobra = altura
    elif y_cobra > altura:
        y_cobra = 0

    if len(lista_cobra) > comprimento_maximo_cobra:
        lista_cobra.pop(0)

    aumenta_cobra(lista_cobra)

    retângulo_texto = texto_formatado.get_rect()
    retângulo_texto.center = (largura // 2, retângulo_texto.height)
    tela.blit(texto_formatado, retângulo_texto)
    pygame.display.update()
