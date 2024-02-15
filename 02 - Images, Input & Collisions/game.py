# --- Importar as bibliotecas --- #
import sys
import pygame


class Jogo:
    """
    Classe responsável pelo jogo.
    """
    def __init__(self):
        """
        Função responsável por inicializar as variáveis.
        """
        # --- Inicializar o Pygame --- #
        pygame.init()

        # --- Colocar um título à janela --- #
        pygame.display.set_caption('Ninja Game')

        # --- Criar a tela --- #
        self.tela = pygame.display.set_mode(
            (
                640,  # largura
                480  # altura
            )
        )

        # --- Criar o "relógio" do ticks do FPS --- #
        self.relogio = pygame.time.Clock()

        # --- Carregar uma imagem --- #
        self.imagem = pygame.image.load('data/images/clouds/cloud_1.png')

        # --- Retirar o fundo da imagem --- #
        self.imagem.set_colorkey((0, 0, 0))

        # --- Posição da imagem --- #
        self.pos_imagem = [160, 260]

        # --- Movimento da imagem --- #
        self.movimento = [False, False]

        # --- Área de colisão --- #
        self.area_colisao = pygame.Rect(
            50,  # posição X
            50,  # posição Y
            300,  # largura
            50  # altura
        )

    def executar(self) -> None:
        """
        Função responsável por executar o código.
        """
        # --- Criar o game loop --- #
        while True:
            # --- Preenher a tela a cada iteração --- #
            self.tela.fill((14, 219, 248))

            # --- Desenhar um retângulo ao redor da imagem --- #
            imagem_rect = pygame.Rect(
                self.pos_imagem[0],  # posição X
                self.pos_imagem[1],  # posição Y
                self.imagem.get_width(),  # largura
                self.imagem.get_height()  # altura
            )

            # --- Verificar se a imagem colidiu com o retângulo --- #
            if imagem_rect.colliderect(self.area_colisao):
                # --- Mudar a cor da área de colisão --- #
                pygame.draw.rect(
                    self.tela,  # tela
                    (0, 100, 255),  # nova cor
                    self.area_colisao  # local que será mudada a cor
                )
            else:
                # --- Caso não colida, mudar para outra cor --- #
                pygame.draw.rect(
                    self.tela,  # tela
                    (0, 50, 155),  # nova cor
                    self.area_colisao  # local que será mudada a cor
                )

            # --- Movimentar a imagem --- #
            self.pos_imagem[1] += (self.movimento[1] - self.movimento[0]) * 5

            # --- Colocar a imagem na tela --- #
            self.tela.blit(
                self.imagem,  # imagem
                self.pos_imagem  # posição
            )

            # --- Obter os eventos do Pygame --- #
            for evento in pygame.event.get():
                # --- Verificar se a tela foi fechada --- #
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # --- Verificar se a tecla foi clicada --- #
                if evento.type == pygame.KEYDOWN:
                    # --- Verificar se a tecla da seta para cima foi clicada --- #
                    if evento.key == pygame.K_UP:
                        self.movimento[0] = True

                    # --- Verificar se a tecla da seta para baixo foi clicada --- #
                    if evento.key == pygame.K_DOWN:
                        self.movimento[1] = True

                # --- Verificar se a tecla foi soltada --- #
                if evento.type == pygame.KEYUP:
                    # --- Verificar se a tecla da seta para cima foi clicada --- #
                    if evento.key == pygame.K_UP:
                        self.movimento[0] = False

                    # --- Verificar se a tecla da seta para baixo foi clicada --- #
                    if evento.key == pygame.K_DOWN:
                        self.movimento[1] = False

            # --- Atualizar a tela --- #
            pygame.display.update()

            # --- Fixar o FPS --- #
            self.relogio.tick(60)


Jogo().executar()
