# --- Importar as bibliotecas --- #
import sys
import pygame
from scripts.nuvens import Nuvens
from scripts.tilemap import Tilemap
from scripts.entidades import FisicaEntidade, Jogador
from scripts.utils import carregar_imagem, carregar_imagens, Animacao


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
            'jogador': carregar_imagem('entities/player.png'),
            'fundo': carregar_imagem('background.png'),
            'nuvem': carregar_imagens('clouds'),
            'jogador/idle': Animacao(carregar_imagens('entities/player/idle'), duracao=6),
            'jogador/correr': Animacao(carregar_imagens('entities/player/run'), duracao=4),
            'jogador/pular': Animacao(carregar_imagens('entities/player/jump')),
            'jogador/slide': Animacao(carregar_imagens('entities/player/slide')),
            'jogador/slide_parede': Animacao(carregar_imagens('entities/player/wall_slide'))
        }

        # --- Nuvens --- #
        self.nuvens = Nuvens(self.assets['nuvem'], quantidade=16)

        # --- Jogador --- #
        self.jogador = Jogador(
            self,
            (50, 50),
            (8, 15)
        )

        # --- Carregar os tiles --- #
        self.tilemap = Tilemap(self, tam_tile=16)

        # --- Scroll da câmera --- #
        self.scroll = [0, 0]

    def executar(self) -> None:
        """
        Função responsável por executar o código.
        """
        # --- Criar o game loop --- #
        while True:
            # --- Colocar o plano de fundo na tela --- #
            self.display.blit(self.assets['fundo'], (0, 0))

            # --- Scroll da câmera segue o jogador --- #
            self.scroll[0] += (self.jogador.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.jogador.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            renderizar_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            # --- Atualizar as nuvens na tela --- #
            self.nuvens.atualizar()

            # --- Renderizar as nuvens na tela --- #
            self.nuvens.renderizar(self.display, deslocamento=renderizar_scroll)

            # --- Renderizar os tiles --- #
            self.tilemap.renderizar(self.display, deslocamento=renderizar_scroll)

            # --- Atualizar o jogador na tela --- #
            self.jogador.atualizar(self.tilemap, (self.movimento[1] - self.movimento[0], 0))

            # --- Renderizar o jogador na tela --- #
            self.jogador.renderizar(self.display, deslocamento=renderizar_scroll)

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
