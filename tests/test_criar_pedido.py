import pytest

from src.app.adapters.controllers.pedido_controller import PedidoController
from src.app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from src.app.dtos.criar_pedido_input_dto import CriarPedidoInputDTO
from src.app.entities.desconto import DescontoVIP
from src.app.entities.pedido import Pedido
from src.app.frameworks.database.memory_database import MemoryDatabase
from src.app.gateways.pedido_gateway import IPedidoGateway
from src.app.presenters.pedido_presenter import PedidoPresenter
from src.app.use_cases.criar_pedido import CriarPedido


class StubPedidoGateway(IPedidoGateway):
    """Dublê do gateway: guarda os pedidos em uma lista, sem banco de dados."""

    def __init__(self):
        self.registros = []

    def salvar(self, pedido, tipo_desconto):
        self.registros.append({"pedido": pedido, "tipo_desconto": tipo_desconto})

    def listar(self):
        return self.registros


def test_entidade_pedido_calcula_valor_final():
    pedido = Pedido("Cliente", 200.0, DescontoVIP())

    assert pedido.valor_desconto() == 40.0
    assert pedido.valor_final() == 160.0


@pytest.mark.parametrize(
    "tipo_desconto, valor_final",
    [("normal", 90.0), ("VIP", 80.0), (" premium ", 70.0)],
)
def test_use_case_aplica_desconto_pelo_tipo(tipo_desconto, valor_final):
    use_case = CriarPedido(StubPedidoGateway())

    output = use_case.executar(CriarPedidoInputDTO("Cliente", 100.0, tipo_desconto))

    assert output.valor_final == valor_final


def test_use_case_salva_pedido_no_gateway():
    gateway = StubPedidoGateway()
    use_case = CriarPedido(gateway)

    use_case.executar(CriarPedidoInputDTO("Cliente", 100.0, "vip"))

    assert len(gateway.registros) == 1
    assert gateway.registros[0]["tipo_desconto"] == "vip"


def test_use_case_rejeita_tipo_de_desconto_invalido():
    use_case = CriarPedido(StubPedidoGateway())

    with pytest.raises(ValueError):
        use_case.executar(CriarPedidoInputDTO("Cliente", 100.0, "ouro"))


def test_use_case_chama_gateway_com_mock(mocker):
    gateway = mocker.Mock(spec=IPedidoGateway)
    use_case = CriarPedido(gateway)

    use_case.executar(CriarPedidoInputDTO("Cliente", 100.0, "normal"))

    gateway.salvar.assert_called_once()


def test_fluxo_completo_criar_e_listar_pedidos():
    database = MemoryDatabase()
    controller = PedidoController(CriarPedido(MemoryPedidoRepository(database)), PedidoPresenter())

    controller.criar_pedido("Cliente A", 100.0, "normal")
    controller.criar_pedido("Cliente B", 100.0, "premium")
    pedidos = controller.listar_pedidos()

    assert [pedido["cliente"] for pedido in pedidos] == ["Cliente A", "Cliente B"]
    assert pedidos[1] == {
        "cliente": "Cliente B",
        "valor_original": 100.0,
        "valor_desconto": 30.0,
        "valor_final": 70.0,
        "tipo_desconto": "premium",
    }
