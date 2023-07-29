# --- Importar as bibliotecas --- #
import sys
import pygame


class Game:
    """Classe responsável por armazenar o jogo."""
    def __init__(self):
        # --- Inicicar o Pygame --- #
        pygame.init()

        # --- Nome do título da janela --- #
        pygame.display.set_caption('Ninja Game')

        # --- Criar a janela --- #
        self.janela = pygame.display.set_mode((640, 480))

        # --- Taxa de FPS --- #
        self.clock = pygame.time.Clock()

        # --- Carregar uma imagem --- #
        self.imagem = pygame.image.load('./data/images/clouds/cloud_1.png')
        self.imagem.set_colorkey((0, 0, 0))  # remove o fundo da imagem baseado no RGB passado

        # --- Movimentação da imagem --- #
        self.imagem_posicao = [160, 260]
        self.movimento = [False, False]  # flags para o movimento no eixo Y e eixo X, respectivamente

        # --- Colisão --- #
        self.colisao_area = pygame.Rect(50, 50, 300, 50)

    def executar(self):
        """Função responsável por rodar o jogo."""
        # --- Game loop --- #
        while True:

            # Preencher a janela com uma cor
            self.janela.fill((14, 219, 248))

            # Rect da imagem
            imagem_rect = pygame.Rect(
                self.imagem_posicao[0],
                self.imagem_posicao[1],
                self.imagem.get_width(),
                self.imagem.get_height()
            )

            # Detectar a colisão
            if imagem_rect.colliderect(self.colisao_area):
                pygame.draw.rect(self.janela, (0, 100, 255), self.colisao_area)
            else:
                pygame.draw.rect(self.janela, (0, 50, 255), self.colisao_area)

            # Movimentar a imagem na tela
            self.imagem_posicao[1] += (self.movimento[1] - self.movimento[
                0]) * 5  # valores booleanos podem ser trasformados para int

            # Colocar a imagem na janela
            self.janela.blit(self.imagem, self.imagem_posicao)

            # Eventos
            for evento in pygame.event.get():
                # Fechar a janela
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Apertar a tecla
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:
                        self.movimento[0] = True
                    if evento.key == pygame.K_DOWN:
                        self.movimento[1] = True

                # Soltar a tecla
                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_UP:
                        self.movimento[0] = False
                    if evento.key == pygame.K_DOWN:
                        self.movimento[1] = False

            # Atualizar a janela
            pygame.display.update()

            # Taxa de FPS
            self.clock.tick(60)


# --- Executar o jogo --- #
Game().executar()
