# --- Importar as bibliotecas --- #
import sys
import pygame
from scripts.tilemap import Tilemap
from scripts.entidades import FisicaEntidade
from scripts.utils import carregar_imagem, carregar_imagens


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

        # --- Criar uma superfície --- #
        self.display = pygame.Surface((320, 240))

        # --- Criar o "relógio" do ticks do FPS --- #
        self.relogio = pygame.time.Clock()

        # --- Movimento da imagem --- #
        self.movimento = [False, False]

        # --- Dicionário com as imagens --- #
        self.assets = {
            'decoracao': carregar_imagens('tiles/decor'),
            'grama': carregar_imagens('tiles/grass'),
            'decoracao_grande': carregar_imagens('tiles/large_decor'),
            'pedra': carregar_imagens('tiles/stone'),
            'jogador': carregar_imagem('entities/player.png')
        }

        # --- Jogador --- #
        self.jogador = FisicaEntidade(
            self,
            'jogador',
            (50, 50),
            (8, 15)
        )

        # --- Carregar os tiles --- #
        self.tilemap = Tilemap(self, tam_tile=16)

    def executar(self) -> None:
        """
        Função responsável por executar o código.
        """
        # --- Criar o game loop --- #
        while True:
            # --- Preenher a tela a cada iteração --- #
            self.display.fill((14, 219, 248))

            # --- Renderizar os tiles --- #
            self.tilemap.renderizar(self.display)

            # --- Atualizar o jogador na tela --- #
            self.jogador.atualizar(self.tilemap, (self.movimento[1] - self.movimento[0], 0))

            # --- Renderizar o jogador na tela --- #
            self.jogador.renderizar(self.display)

            # --- Obter os eventos do Pygame --- #
            for evento in pygame.event.get():
                # --- Verificar se a tela foi fechada --- #
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # --- Verificar se a tecla foi clicada --- #
                if evento.type == pygame.KEYDOWN:
                    # --- Verificar se a tecla da seta para esquerda foi clicada --- #
                    if evento.key == pygame.K_LEFT:
                        self.movimento[0] = True

                    # --- Verificar se a tecla da seta para direita foi clicada --- #
                    if evento.key == pygame.K_RIGHT:
                        self.movimento[1] = True

                    # --- Verificar se a tecla para cima foi clicada --- #
                    if evento.key == pygame.K_UP:
                        self.jogador.velocidade[1] = -3

                # --- Verificar se a tecla foi soltada --- #
                if evento.type == pygame.KEYUP:
                    # --- Verificar se a tecla da seta para esquerda foi clicada --- #
                    if evento.key == pygame.K_LEFT:
                        self.movimento[0] = False

                    # --- Verificar se a tecla da seta para direita foi clicada --- #
                    if evento.key == pygame.K_RIGHT:
                        self.movimento[1] = False

            # --- Aumentar o tamanho do display para que os sprites fiquem maiores --- #
            self.tela.blit(
                pygame.transform.scale(
                    self.display,  # a superfície a ser aumentada
                    self.tela.get_size()  # tamanho final
                ),
                (0, 0)
            )

            # --- Atualizar a tela --- #
            pygame.display.update()

            # --- Fixar o FPS --- #
            self.relogio.tick(60)


Jogo().executar()
