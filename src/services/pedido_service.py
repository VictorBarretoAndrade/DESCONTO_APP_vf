from src.models.pedido import Pedido


class PedidoService:
    """Classe de serviço para processar pedidos e aplicar descontos."""

    def __init__(self) -> None:
        self.pedidos: list[Pedido] = []

    def adicionar_pedido(self, pedido: Pedido) -> None:
        self.pedidos.append(pedido)

    def processar_pedidos(self) -> None:
        for pedido in self.pedidos:
            print(f"Cliente: {pedido.cliente}")
            print(f"Valor final: {pedido.valor_final(pedido.valor_original)}")
