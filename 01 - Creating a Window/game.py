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

    def executar(self):
        """Função responsável por rodar o jogo."""
        # --- Game loop --- #
        while True:
            # Eventos
            for evento in pygame.event.get():
                # Fechar a janela
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Atualizar a janela
            pygame.display.update()

            # Taxa de FPS
            self.clock.tick(60)


# --- Executar o jogo --- #
Game().executar()
