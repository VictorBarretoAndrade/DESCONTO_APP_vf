import abc
from typing import TypedDict

from src.app.entities.pedido import Pedido


class RegistroPedido(TypedDict):
    pedido: Pedido
    tipo_desconto: str


class IPedidoGateway(abc.ABC):
    @abc.abstractmethod
    def salvar(self, pedido: Pedido, tipo_desconto: str) -> None:
        pass

    @abc.abstractmethod
    def listar(self) -> list[RegistroPedido]:
        pass
