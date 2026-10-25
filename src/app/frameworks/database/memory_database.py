from src.app.gateways.pedido_gateway import RegistroPedido


class MemoryDatabase:
    def __init__(self) -> None:
        self.pedidos: list[RegistroPedido] = []
