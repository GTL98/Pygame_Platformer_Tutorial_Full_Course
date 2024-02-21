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
    :param caminho: Caminho da imagem.
    :return: Imagem carregada.
    """
    # --- Lista com as imagens --- #
    imagens = []

    # --- Iterar sobre cada imagem --- #
    for nome_imagem in sorted(os.listdir(CAMINHO_BASE + caminho)):
        # --- Carregar e adicionas cada imagem presente na pasta --- #
        imagens.append(carregar_imagem(caminho + '/' + nome_imagem))

    return imagens
