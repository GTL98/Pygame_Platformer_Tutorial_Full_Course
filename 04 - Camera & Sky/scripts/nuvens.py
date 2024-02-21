# --- Importar a biblioteca --- #
import random


class Nuvem:
    """
    Classe reponsável por criar a nuven.
    """
    def __init__(self, posicao, imagem, velocidade, profundidade):
        """
        Função responsável por inicializar a classe.
        :param posicao: Posição da nuvem na tela.
        :param imagem: Qual imagem da nuvem a ser usada.
        :param velocidade: Velocidade de movimento da nuvem.
        :param profundidade: Profundidade da nuvens no céu para o efeito de parallax.
        """
        self.posicao = list(posicao)
        self.imagem = imagem
        self.velocidade = velocidade
        self.profundidade = profundidade

    def atualizar(self) -> None:
        """
        Função responsável por atualizar a nuvem.
        """
        # --- Atualizar a posição --- #
        self.posicao[0] += self.velocidade

    def renderizar(self, superficie, deslocamento=(0, 0)) -> None:
        """
        Função responsável por renderizar a nuvem.
        :param superficie: Superfície onde a nuvem será renderizado.
        :param deslocamento: Scroll do mapa.
        """
        # --- Renderizar a posição --- #
        renderizar_posicao = (
            self.posicao[0] - deslocamento[0] * self.profundidade,  # isso cria um efeito de parallax
            self.posicao[1] - deslocamento[1] * self.profundidade
        )

        # --- Colocar a imagem na tela --- #
        superficie.blit(
            self.imagem,
            (renderizar_posicao[0] % (superficie.get_width() + self.imagem.get_width()) - self.imagem.get_width(),
             renderizar_posicao[1] % (superficie.get_height() + self.imagem.get_height()) - self.imagem.get_height()
             )
        )


class Nuvens:
    """
    Classe responsável por criar as nuvens.
    """
    def __init__(self, imagens_nuvem, quantidade=16):
        """
        Funão responsável por inicializar a classe.
        :param imagens_nuvem: Sprites das nuvens.
        :param quantidade: Quantidade de nuvens na tela.
        """
        # --- Lista para armazenar as nuvens --- #
        self.nuvens = []

        # --- Adicionar à lista as nuvens criadas --- #
        for i in range(quantidade):
            # --- Posição da nuvem --- #
            posicao = (random.random() * 99999, random.random() * 99999)

            # --- Escolher uma nuvem --- #
            imagem = random.choice(imagens_nuvem)

            # --- Velocidade da nuvem --- #
            velocidade = random.random() * 0.05 + 0.05

            # --- Profundidade da nuvem --- #
            profundidade = random.random() * 0.6 + 0.02

            self.nuvens.append(
                Nuvem(
                    posicao,
                    imagem,
                    velocidade,
                    profundidade
                )
            )

        # --- Organizar as nuvens pela profunsidade --- #
        self.nuvens.sort(key=lambda x: x.profundidade)

    def atualizar(self) -> None:
        """
        Função responsável por atualizar as nuvens.
        """
        for nuvem in self.nuvens:
            nuvem.atualizar()

    def renderizar(self, superficie, deslocamento=(0, 0)) -> None:
        """
        Função responsável por renderizar as nuvens.
        :param superficie: Superfície onde as nuvens serão renderizadas.
        :param deslocamento: Scroll do mapa.
        """
        for nuvem in self.nuvens:
            nuvem.renderizar(superficie, deslocamento=deslocamento)
