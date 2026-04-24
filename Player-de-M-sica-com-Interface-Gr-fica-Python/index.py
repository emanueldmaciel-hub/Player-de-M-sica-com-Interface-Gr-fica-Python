import pygame
import sys

# Inicialização
pygame.init()
pygame.mixer.init()

# Configurações da tela
LARGURA, ALTURA = 600, 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Player com Texto e Volume")

# Cores
BRANCO = (255, 255, 255)
CINZA = (40, 40, 40)
VERDE = (0, 200, 0)

# Fonte
fonte = pygame.font.SysFont("Arial", 30, bold=True)
fonte_pequena = pygame.font.SysFont("Arial", 20)

# Música
pygame.mixer.music.load("musica.mp3")  # coloque seu arquivo aqui
pygame.mixer.music.play()

# Volume inicial
volume = 0.25
pygame.mixer.music.set_volume(volume)

# Fundo (com fallback)
try:
    fundo_img = pygame.image.load("Canon inD.jpg")
    fundo = pygame.transform.smoothscale(fundo_img, (LARGURA, ALTURA))
except:
    fundo = pygame.Surface((LARGURA, ALTURA))
    fundo.fill(CINZA)

# Nome da música
nome_musica = "Canon in D"

# Loop principal
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                volume = min(1.0, volume + 0.05)
                pygame.mixer.music.set_volume(volume)

            if event.key == pygame.K_DOWN:
                volume = max(0.0, volume - 0.05)
                pygame.mixer.music.set_volume(volume)

            if event.key == pygame.K_p:
                pygame.mixer.music.pause()

            if event.key == pygame.K_r:
                pygame.mixer.music.unpause()

            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
                rodando = False

    # ===== DESENHO =====
    # 1. Fundo
    tela.blit(fundo, (0, 0))

    # 2. Barra de volume
    barra_x = 150
    barra_y = 200
    barra_largura = 300
    barra_altura = 20

    # Borda
    pygame.draw.rect(tela, BRANCO, (barra_x, barra_y, barra_largura, barra_altura), 2)

    # Preenchimento
    largura_preenchida = int(barra_largura * volume)
    pygame.draw.rect(tela, VERDE, (barra_x, barra_y, largura_preenchida, barra_altura))

    # 3. Textos
    # Nome da música (centralizado)
    texto_nome = fonte.render(nome_musica, True, BRANCO)
    x_nome = (LARGURA - texto_nome.get_width()) // 2
    tela.blit(texto_nome, (x_nome, 100))

    # Volume
    texto_volume = fonte_pequena.render(f"Volume: {int(volume*100)}%", True, BRANCO)
    tela.blit(texto_volume, (barra_x, barra_y + 30))

    # 4. Atualizar tela
    pygame.display.flip()

# Encerramento
pygame.quit()
sys.exit()