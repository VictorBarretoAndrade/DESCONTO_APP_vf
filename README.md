# DESCONTO_APP_vf

Sistema de pedidos com descontos desenvolvido na disciplina AQS (Alta Qualidade em Software).

Uma loja precisa receber pedidos de clientes, aplicar desconto conforme o tipo de cliente
(normal, VIP ou premium), salvar os pedidos e listar os pedidos já registrados.

## Como executar

```bash
python -m venv .venv
.\.venv\Scripts\activate
python main.py
```

## Testes e análise estática

```bash
pip install -r requirements-dev.txt
pytest -v
ruff check .
mypy --strict src main.py
```

## Arquitetura Limpa (`src/app`)

As regras de negócio não dependem de banco, framework, tela ou biblioteca externa.
As dependências apontam sempre para dentro (das bordas para as entidades).

| Camada | Pasta | Responsabilidade |
| --- | --- | --- |
| Entities | `entities` | Regras de negócio puras (`Pedido`, descontos) |
| Use Cases | `use_cases` | `CriarPedido`: coordena o fluxo de criar e listar pedidos |
| Gateways | `gateways` | `IPedidoGateway`: contrato para salvar e listar pedidos |
| DTOs | `dtos` | Objetos de entrada e saída que trafegam entre as camadas |
| Repository Adapter | `adapters/repositories` | `MemoryPedidoRepository`: implementa o gateway |
| Controller | `adapters/controllers` | `PedidoController`: porta de entrada, apenas encaminha |
| Presenter | `presenters` | `PedidoPresenter`: formata a saída para exibição |
| Frameworks & Drivers | `frameworks/database` | `MemoryDatabase`: armazenamento em memória |

Fluxo: `main` → `PedidoController` → `CriarPedido` → `IPedidoGateway` (`MemoryPedidoRepository`)
→ `MemoryDatabase`; a resposta volta como `CriarPedidoOutputDTO` e é formatada pelo `PedidoPresenter`.

A versão anterior, em arquitetura de camadas (controllers, services, repositories, database
e models), foi mantida em `src_antigo` para comparação.
