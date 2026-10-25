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

## Arquitetura em camadas

| Camada | Pasta | Responsabilidade |
| --- | --- | --- |
| Controller | `src/controllers` | Recebe as entradas e encaminha para os serviços |
| Service | `src/services` | Regras de negócio (aplicar descontos, processar pedidos) |
| Repository | `src/repositories` | Abstrai o acesso aos dados |
| Database | `src/database` | Infraestrutura de conexão com o banco |
| Models | `src/models` | Estrutura dos dados (`Pedido`, descontos) |
