# --- Importar as bibliotecas --- #
import pygame
from typing import List, Dict

# --- Contantes --- #
DESLOCAMENTOS_VIZIHOS = [
    (-1, 0), (-1, -1), (0, -1),
    (1, -1), (1, 0), (0, 0),
    (-1, 1), (0, 1), (1, 1)
]
FISICA_TILES = {
    'grama',
    'pedra'
}


class Tilemap:
    """
    Classe responsável pelo tiles do mapa.
    """
    def __init__(self, jogo, tam_tile=16):
        """
        Função responsável por inicializar a classe.
        :param jogo: Classe do jogo.
        :param tam_tile: Tamanho do tile.
        """
        self.jogo = jogo
        self.tam_tile = tam_tile
        self.tilemap = {}  # armazenar as informações do tiles
        self.offgrid_tiles = []  # armazenar os tiles

        # --- Adicionar ao dicionário os tiles do mapa --- #
        for i in range(10):
            self.tilemap[str(3 + i) + ';10'] = {
                'tipo': 'grama',
                'variante': 1,
                'pos': (3 + i, 10)
            }
            self.tilemap['10;' + str(i + 5)] = {
                'tipo': 'pedra',
                'variante': 1,
                'pos': (10, i + 5)
            }

    def tiles_entorno(self, posicao) -> List[Dict]:
        """
        Função responsável por mapear os tiles vizinhos quando um tile encontra com outro.
        :param posicao: Posição dos tiles vizinhos.
        :return: Lista com as informações dos tiles.
        """
        # --- Criar uma lista para armazenar os tiles checados --- #
        tiles = []

        # --- Converter a posição de pixel para o grid da tela --- #
        loc_tile = (int(posicao[0] // self.tam_tile), int(posicao[1] // self.tam_tile))

        # --- Checar os tiles no entorno do tile analisado --- #
        for deslocamento in DESLOCAMENTOS_VIZIHOS:
            checar_loc = str(loc_tile[0] + deslocamento[0]) + ';' + str(loc_tile[1] + deslocamento[1])

            # --- Verificar se o tile está presente no dicionário --- #
            if checar_loc in self.tilemap:
                tiles.append(self.tilemap[checar_loc])

        return tiles

    def fisica_tiles_entorno(self, posicao) -> List[object]:
        """
        Função responsável por aplicar a física quando um tile encontra o outro.
        :param posicao: Posição do tile.
        :return: Lista com o objeto rect de cada tile interagido.
        """
        # --- Criar uma lista com os rects dos tiles --- #
        rects = []

        # --- Iterar sobre cada tile no entorno --- #
        for tile in self.tiles_entorno(posicao):
            # --- Verificar se o tile possui física --- #
            if tile['tipo'] in FISICA_TILES:
                # --- Adicionar o rect do tile --- #
                rects.append(
                    pygame.Rect(
                        tile['pos'][0] * self.tam_tile,  # posição X
                        tile['pos'][1] * self.tam_tile,  # posição Y
                        self.tam_tile,  # largura
                        self.tam_tile  # altura
                    )
                )

        return rects

    def renderizar(self, superficie) -> None:
        """
        Função responsável por renderizar os tiles.
        :param superficie: Superfície onde o tile será renderizado.
        """
        for tile in self.offgrid_tiles:
            superficie.blit(
                self.jogo.assets[tile['tipo']['variante']],
                tile['pos']
            )
        # --- Iterar sobre cada item do dicionário --- #
        for loc in self.tilemap:
            # --- Obter a localização de cada tile --- #
            tile = self.tilemap[loc]

            # --- Colocar na tela o tile --- #
            superficie.blit(
                self.jogo.assets[tile['tipo']][tile['variante']],
                (
                        tile['pos'][0] * self.tam_tile,
                        tile['pos'][1] * self.tam_tile
                )
            )
