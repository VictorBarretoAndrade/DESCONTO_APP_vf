from src.app.entities.desconto import DescontoNormal, DescontoPremium, DescontoVIP, IDesconto
from src.app.entities.pedido import Pedido
from src.app.gateways.pedido_gateway import IPedidoGateway


class CriarPedido:
    def __init__(self, pedido_gateway: IPedidoGateway) -> None:
        # O Use Case depende da abstração (gateway), e não da implementação
        self.pedido_gateway = pedido_gateway

    def executar(self, cliente: str, valor_original: float, tipo_desconto: str) -> Pedido:
        desconto: IDesconto
        if tipo_desconto.lower() == "normal":
            desconto = DescontoNormal()
        elif tipo_desconto.lower() == "vip":
            desconto = DescontoVIP()
        elif tipo_desconto.lower() == "premium":
            desconto = DescontoPremium()
        else:
            raise ValueError("Tipo de desconto inválido")

        pedido = Pedido(cliente, valor_original, desconto)
        self.pedido_gateway.salvar(pedido, tipo_desconto)

        return pedido

    def listar_pedidos(self) -> list[Pedido]:
        return [registro["pedido"] for registro in self.pedido_gateway.listar()]
