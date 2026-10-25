from src.models.desconto import DescontoNormal, DescontoPremium, DescontoVIP
from src.models.pedido import Pedido
from src.repositories.pedido_repository import PedidoRepository
from src.services.pedido_service import PedidoService

if __name__ == "__main__":
    # Configuração do repositório e serviço
    repo = PedidoRepository()
    service = PedidoService(repo)

    pedido1 = Pedido("Leonardo", DescontoNormal())
    pedido1.valor_original = 100.0
    pedido2 = Pedido("Cardia", DescontoVIP())
    pedido2.valor_original = 100.0
    pedido3 = Pedido("Da Cruz", DescontoPremium())
    pedido3.valor_original = 100.0

    service.adicionar_pedido(pedido1)
    service.adicionar_pedido(pedido2)
    service.adicionar_pedido(pedido3)

    service.processar_pedidos()
