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

    def executar(self) -> None:
        """
        Função responsável por executar o código.
        """
        # --- Criar o game loop --- #
        while True:
            # --- Obter os eventos do Pygame --- #
            for evento in pygame.event.get():
                # --- Verificar se a tela foi fechada --- #
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # --- Atualizar a tela --- #
            pygame.display.update()

            # --- Fixar o FPS --- #
            self.relogio.tick(60)


Jogo().executar()
