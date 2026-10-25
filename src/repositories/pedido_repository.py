from src.models.pedido import Pedido


class PedidoRepository:
    """Classe de repositório para armazenar e gerenciar pedidos."""

    def __init__(self) -> None:
        self.pedidos: list[Pedido] = []

    def adicionar_pedido(self, pedido: Pedido) -> None:
        self.pedidos.append(pedido)

    def listar_pedidos(self) -> list[Pedido]:
        return self.pedidos
