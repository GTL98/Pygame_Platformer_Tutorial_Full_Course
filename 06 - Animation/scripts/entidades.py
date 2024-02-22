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
        self.acao = ''
        self.deslocamento_animacao = (-3, -3)  # como o sprite é menor que a imagem, precisa ajustar
        self.flip = False
        self.acao_escolhida('idle')

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

    def acao_escolhida(self, acao) -> None:
        """
        Função responsável por escolher a ação do jogador.
        :param acao: Ação do jogador.
        """
        # --- Verificar a ação do jogador --- #
        if acao != self.acao:
            self.acao = acao
            self.animacao = self.jogo.assets[self.tipo + '/' + self.acao].copiar()

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

        # --- Verificar se o jogador está para a direita --- #
        if movimento[0] > 0:
            self.flip = False

        # --- Verificar se o jogador está para a esquerda --- #
        if movimento[0] < 0:
            self.flip = True

        # --- Aplicar a gravidade --- #
        self.velocidade[1] = min(5.0, self.velocidade[1] + 0.1)

        # --- Verificar se o jogador pulou ou aterrisou --- #
        if self.colisao['baixo'] or self.colisao['cima']:
            self.velocidade[1] = 0

        # --- Atualizar a animação --- #
        self.animacao.atualizar()

    def renderizar(self, superficie, deslocamento=(0, 0)) -> None:
        """
        Função responsável por renderizar a entidade.
        :param superficie: Superfície onde a entidade será renderizada.
        :param deslocamento: Scroll do mapa.
        """
        # --- Colocar o sprite de uma determinada entidade da tela --- #
        superficie.blit(
            pygame.transform.flip(
                self.animacao.imagem(),  # imagem
                self.flip,  # flip no eixo X
                False  # flip no eixo Y
            ),
            (self.posicao[0] - deslocamento[0] + self.deslocamento_animacao[0],
             self.posicao[1] - deslocamento[1] + self.deslocamento_animacao[1]
             )
        )


class Jogador(FisicaEntidade):
    """
    Função responsável por criar o jogador.
    """
    def __init__(self, jogo, posicao, tamanho):
        """
        Função responsável por inicializar a classe.
        :param jogo: Classe do jogo.
        :param posicao: Posição do sprite do jogador.
        :param tamanho: Tamanho do sprite do jogador
        """
        super().__init__(jogo, 'jogador', posicao, tamanho)
        self.tempo_ar = 0

    def atualizar(self, tilemap, movimento=(0, 0)) -> None:
        """
        Função responsável por atualizar o jogador.
        :param tilemap: Tiles do jogo.
        :param movimento: Movimento do jogador.
        """
        # --- Atualizar o jogador --- #
        super().atualizar(tilemap, movimento=movimento)

        # --- Adicionar o tempo no ar do jogador --- #
        self.tempo_ar += 1

        # --- Verificar se o jogador está no chão --- #
        if self.colisao['baixo']:
            self.tempo_ar = 0

        # --- Verificar se o jogador pulou --- #
        if self.tempo_ar > 4:
            self.acao_escolhida('pular')

        # --- Verificar se o jogador está se movimentando no eixo X --- #
        elif movimento[0] != 0:
            self.acao_escolhida('correr')

        # --- Verificar se o jogador está parado --- #
        else:
            self.acao_escolhida('idle')
