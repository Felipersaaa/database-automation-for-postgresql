# Automação de Backup para PostgreSQL

Script em Python para automatizar o backup de bancos de dados PostgreSQL usando o `pg_dump`.

## O que o script faz

- Conecta em um servidor PostgreSQL
- Gera um arquivo `.sql` com o backup do banco escolhido
- Salva o arquivo com data e hora no nome (exemplo: `backup_20261105_091900.sql`)
- Cria a pasta de destino automaticamente, se ela não existir

## Requisitos

- Python 3.6 ou superior
- PostgreSQL instalado (o comando `pg_dump` precisa estar disponível no terminal)
- Permissão de acesso ao banco de dados

## Como usar

Execute no terminal:

    python backup-script-pgsql.py --host localhost --db meu_banco --output ./backups

### Parâmetros

| Parâmetro | Descrição | Obrigatório |
|-----------|-----------|-------------|
| `--host` | Endereço do servidor PostgreSQL | Sim |
| `--db` | Nome do banco de dados | Sim |
| `--output` | Pasta onde o backup será salvo | Sim |

## Observações

- O script usa o usuário `postgres` por padrão.
- Se o servidor pedir senha, ela será solicitada no terminal.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
