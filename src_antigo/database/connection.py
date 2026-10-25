from src_antigo.models.pedido import Pedido


class DatabaseConnection:
    """Classe de conexão com o banco de dados."""

    def __init__(self) -> None:
        self.pedidos: list[Pedido] = []
