from src.app.entities.pedido import Pedido


class MemoryDatabase:
    def __init__(self) -> None:
        self.pedidos: list[Pedido] = []
