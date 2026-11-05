# Automação de Backup para PostgreSQL

Script em Python para automatizar o backup de bancos de dados PostgreSQL usando o `pg_dump`.

## O que o script faz

- Conecta em um servidor PostgreSQL
- Gera um arquivo `.sql` com o backup do banco escolhido
- Salva o arquivo com nome do banco, data e hora (exemplo: `backup_meu_banco_20261105_091900.sql`)
- Cria a pasta de destino automaticamente, se ela não existir
- Avisa com mensagem clara se o `pg_dump` não estiver instalado ou se o backup falhar

## Requisitos

- Python 3.6 ou superior
- PostgreSQL instalado (o comando `pg_dump` precisa estar disponível no terminal)
- Permissão de acesso ao banco de dados

## Como usar

Execute no terminal:

    python backup-script-pgsql.py --host localhost --db meu_banco --output ./backups

Com usuário e porta diferentes do padrão:

    python backup-script-pgsql.py --host localhost --db meu_banco --output ./backups --user meu_usuario --port 5433

### Parâmetros

| Parâmetro | Descrição | Obrigatório | Padrão |
|-----------|-----------|-------------|--------|
| `--host` | Endereço do servidor PostgreSQL | Sim | - |
| `--db` | Nome do banco de dados | Sim | - |
| `--output` | Pasta onde o backup será salvo | Sim | - |
| `--user` | Usuário do PostgreSQL | Não | `postgres` |
| `--port` | Porta do PostgreSQL | Não | `5432` |

## Senha

O script não recebe a senha como parâmetro, para ela não ficar salva no histórico do terminal. Se o servidor exigir senha, o `pg_dump` vai pedir no terminal na hora de rodar.

Para automatizar sem digitar a senha, use a variável de ambiente `PGPASSWORD` ou o arquivo `.pgpass` do PostgreSQL.

## Segurança

- O script não usa `shell=True`, então os parâmetros não podem ser usados para injetar comandos.
- Os arquivos `.sql` e a pasta `backups/` estão no `.gitignore`, para não irem para o GitHub por engano.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
