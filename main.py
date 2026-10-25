from src.app.adapters.controllers.pedido_controller import PedidoController
from src.app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from src.app.frameworks.database.memory_database import MemoryDatabase
from src.app.presenters.pedido_presenter import PedidoPresenter
from src.app.use_cases.criar_pedido import CriarPedido


def criar_controller() -> PedidoController:
    """Monta todas as camadas: database -> repository (gateway) -> use case -> controller."""
    database = MemoryDatabase()
    pedido_gateway = MemoryPedidoRepository(database)
    criar_pedido_use_case = CriarPedido(pedido_gateway)
    presenter = PedidoPresenter()
    return PedidoController(criar_pedido_use_case, presenter)


def main() -> None:
    controller = criar_controller()

    # Criando os pedidos e calculando os descontos
    print("Pedidos criados:")
    for cliente, valor_original, tipo_desconto in [
        ("Cliente A", 100.0, "normal"),
        ("Cliente B", 200.0, "vip"),
        ("Cliente C", 300.0, "premium"),
    ]:
        pedido = controller.criar_pedido(cliente, valor_original, tipo_desconto)
        print(
            f"- {pedido['cliente']}: R$ {pedido['valor_original']:.2f} "
            f"({pedido['tipo_desconto']}) -> R$ {pedido['valor_final']:.2f}"
        )

    # Listando todos os pedidos já realizados
    print("\nPedidos registrados:")
    for pedido in controller.listar_pedidos():
        print(
            f"Cliente: {pedido['cliente']} | Tipo: {pedido['tipo_desconto']} | "
            f"Valor original: R$ {pedido['valor_original']:.2f} | "
            f"Desconto: R$ {pedido['valor_desconto']:.2f} | "
            f"Valor final: R$ {pedido['valor_final']:.2f}"
        )


if __name__ == "__main__":
    main()
