# --- Importar as bibliotecas --- #
import os
import pygame
from typing import List

# --- Definir o caminho base --- #
CAMINHO_BASE = 'data/images/'


def carregar_imagem(caminho: str) -> object:
    """
    Função responsável por carregar uma imagem.
    :param caminho: Caminho da imagem.
    :return: Imagem carregada.
    """
    # --- Carregar a imagem --- #
    imagem = pygame.image.load(CAMINHO_BASE + caminho).convert()

    # --- Retirar o fundo da imagem --- #
    imagem.set_colorkey((0, 0, 0))

    return imagem


def carregar_imagens(caminho: str) -> List[object]:
    """
    Função responsável por carregar várias imagens.
    :param caminho: Caminho das imagens.
    :return: Imagens carregadas.
    """
    # --- Lista com as imagens --- #
    imagens = []

    # --- Iterar sobre cada imagem --- #
    for nome_imagem in sorted(os.listdir(CAMINHO_BASE + caminho)):
        # --- Carregar e adicionas cada imagem presente na pasta --- #
        imagens.append(carregar_imagem(caminho + '/' + nome_imagem))

    return imagens


class Animacao:
    """
    Classe responsável pela animamação.
    """
    def __init__(self, imagens, duracao=5, loop=True):
        """
        Função responsável por inicializar a classe.
        :param imagens: Imagens para a animação.
        :param duracao: Duração da animação.
        :param loop: Se a animação ficará em loop ou não.
        """
        self.imagens = imagens
        self.duracao = duracao
        self.loop = loop
        self.feito = False
        self.frame = 0

    def copiar(self) -> object:
        """
        Função responsável por copiar as animações.
        :return: Classe da animação.
        """
        return Animacao(self.imagens, self.duracao, self.loop)

    def atualizar(self) -> None:
        """
        Função responsável por atualizar a animação.
        """
        # --- Criar a animação --- #
        if self.loop:
            self.frame = (self.frame + 1) % (self.duracao * len(self.imagens))
        else:
            self.frame = min(self.frame + 1, self.duracao * len(self.imagens) - 1)
            # --- Verificar se a animação já terminou --- #
            if self.frame >= self.duracao * len(self.imagens) - 1:
                self.feito = True

    def imagem(self) -> object:
        """
        Função responsável por selecionar a imagem correspondente ao frame.
        :return: Imagem correta do frame.
        """
        return self.imagens[int(self.frame / self.duracao)]