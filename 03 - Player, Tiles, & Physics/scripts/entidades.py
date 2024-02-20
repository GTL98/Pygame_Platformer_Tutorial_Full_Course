# --- Importar a biblioteca --- #
import pygame


class FisicaEntidade:
    """
    Classe responsável pela física das entidades.
    """
    def __init__(self, jogo, tipo_entidade, posicao, tamanho):
        """
        Função responsável por inicializar as variáveis da classe.
        :param jogo: Classe do jogo.
        :param tipo_entidade: Tipo da entidade.
        :param posicao: Posição da entidade.
        :param tamanho: Tamanho da entidade.
        """
        self.jogo = jogo
        self.tipo = tipo_entidade
        self.posicao = list(posicao)
        self.tamanho = tamanho
        self.velocidade = [0, 0]
        self.colisao = {
            'cima': False,
            'baixo': False,
            'direita': False,
            'esquerda': False
        }

    def rect(self) -> object:
        """
        Função responsável por criar os rects dos tiles do mapa.
        :return: Rects dos tiles.
        """
        return pygame.Rect(
            self.posicao[0],  # posição X
            self.posicao[1],  # posição Y
            self.tamanho[0],  # largura
            self.tamanho[1]  # altura
        )

    def atualizar(self, tilemap, movimento=(0, 0)) -> None:
        """
        Função responsável por atualizar a entidade.
        :param tilemap: Tiles do mapa.
        :param movimento: Movimento da entidade.
        """
        # --- Dicionário com as possíveis colisões --- #
        self.colisao = {
            'cima': False,
            'baixo': False,
            'direita': False,
            'esquerda': False
        }

        # --- Movimento do frame --- #
        movimento_frame = (movimento[0] + self.velocidade[0], movimento[1] + self.velocidade[1])

        # --- Atualizar a posição no eixo X--- #
        self.posicao[0] += movimento_frame[0]

        # --- Verificar a colisão do jogador com os tiles no eixo X --- #
        rect_entidade = self.rect()
        for rect in tilemap.fisica_tiles_entorno(self.posicao):
            if rect_entidade.colliderect(rect):
                # --- Encontrou um tile à direita --- #
                if movimento_frame[0] > 0:
                    rect_entidade.right = rect.left
                    self.colisao['direita'] = True

                # --- Encontrou um tile à esquerda --- #
                if movimento_frame[0] < 0:
                    rect_entidade.left = rect.right
                    self.colisao['esquerda'] = True

                # --- Evita erros com valores float da posição --- #
                self.posicao[0] = rect_entidade.x

        # --- Atualizar a posição no eixo Y --- #
        self.posicao[1] += movimento_frame[1]

        # --- Verificar a colisão do jogador com os tiles no eixo Y --- #
        rect_entidade = self.rect()
        for rect in tilemap.fisica_tiles_entorno(self.posicao):
            if rect_entidade.colliderect(rect):
                # --- Encontrou um tile abaixo --- #
                if movimento_frame[1] > 0:
                    rect_entidade.bottom = rect.top
                    self.colisao['baixo'] = True

                # --- Encontrou um tile acima --- #
                if movimento_frame[1] < 0:
                    rect_entidade.top = rect.bottom
                    self.colisao['cima'] = True

                # --- Evita erros com valores float da posição --- #
                self.posicao[1] = rect_entidade.y

        # --- Aplicar a gravidade --- #
        self.velocidade[1] = min(5.0, self.velocidade[1] + 0.1)

        # --- Verificar se o jogador pulou ou aterrisou --- #
        if self.colisao['baixo'] or self.colisao['cima']:
            self.velocidade[1] = 0

    def renderizar(self, superficie) -> None:
        """
        Função responsável por renderizar a entidade.
        :param superficie: Superfície onde a entidade será renderizada.
        """
        # --- Colocar o sprite de uma determinada entidade da tela --- #
        superficie.blit(self.jogo.assets['jogador'], self.posicao)
