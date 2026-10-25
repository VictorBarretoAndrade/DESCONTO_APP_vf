from src.app.dtos.criar_pedido_input_dto import CriarPedidoInputDTO
from src.app.dtos.criar_pedido_output_dto import CriarPedidoOutputDTO
from src.app.use_cases.criar_pedido import CriarPedido


class PedidoController:
    def __init__(self, criar_pedido_use_case: CriarPedido) -> None:
        self.criar_pedido_use_case = criar_pedido_use_case

    def criar_pedido(
        self, cliente: str, valor_original: float, tipo_desconto: str
    ) -> CriarPedidoOutputDTO:
        input_dto = CriarPedidoInputDTO(
            cliente=cliente,
            valor_original=valor_original,
            tipo_desconto=tipo_desconto,
        )

        return self.criar_pedido_use_case.executar(input_dto)

    def listar_pedidos(self) -> list[CriarPedidoOutputDTO]:
        return self.criar_pedido_use_case.listar_pedidos()
