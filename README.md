# Automação de Backup para PostgreSQL

Scripts em Python para automatizar o backup e a restauração de bancos de dados PostgreSQL usando `pg_dump` e `psql`.

## O que os scripts fazem

- Conectam em um servidor PostgreSQL
- Geram um arquivo `.sql` com o backup do banco escolhido
- Salvam o arquivo com nome do banco, data e hora (exemplo: `backup_meu_banco_20261105_091900.sql`)
- Criam a pasta de destino automaticamente, se ela não existir
- Avisam com mensagem clara se o `pg_dump` ou o `psql` não estiverem instalados, ou se a operação falhar

## Requisitos

- Python 3.6 ou superior
- PostgreSQL instalado (os comandos `pg_dump` e `psql` precisam estar disponíveis no terminal)
- Permissão de acesso ao banco de dados

## Como usar

Execute no terminal:

```bash
python backup-script-pgsql.py --host localhost --db meu_banco --output ./backups
```

Com usuário e porta diferentes do padrão:

```bash
python backup-script-pgsql.py --host localhost --db meu_banco --output ./backups --user meu_usuario --port 5433
```

### Parâmetros do backup

| Parâmetro | Descrição | Obrigatório | Padrão |
|-----------|-----------|-------------|--------|
| `--host` | Endereço do servidor PostgreSQL | Sim | - |
| `--db` | Nome do banco de dados | Sim | - |
| `--output` | Pasta onde o backup será salvo | Sim | - |
| `--user` | Usuário do PostgreSQL | Não | `postgres` |
| `--port` | Porta do PostgreSQL | Não | `5432` |

## Restauração

Para restaurar um backup em um banco existente (e vazio):

```bash
python restore-script-pgsql.py --host localhost --db banco_destino --file ./backups/backup_meu_banco_20261105_193129.sql
```

### Parâmetros da restauração

| Parâmetro | Descrição | Obrigatório | Padrão |
|-----------|-----------|-------------|--------|
| `--host` | Endereço do servidor PostgreSQL | Sim | - |
| `--db` | Banco de destino (precisa existir) | Sim | - |
| `--file` | Arquivo `.sql` gerado pelo backup | Sim | - |
| `--user` | Usuário do PostgreSQL | Não | `postgres` |
| `--port` | Porta do PostgreSQL | Não | `5432` |

## Senha

Os scripts não recebem a senha como parâmetro, para ela não ficar salva no histórico do terminal. Se o servidor exigir senha, o `pg_dump` (ou o `psql`) vai pedir no terminal na hora de rodar.

Para automatizar sem digitar a senha, use a variável de ambiente `PGPASSWORD` ou o arquivo `.pgpass` do PostgreSQL.

## Exemplo completo no Windows (PowerShell)

```powershell
$env:PGPASSWORD = "sua_senha"
python backup-script-pgsql.py --host localhost --db meubanco --output C:\Backups
python restore-script-pgsql.py --host localhost --db banco_destino --file C:\Backups\NOME_DO_ARQUIVO.sql
```

A senha fica só na janela atual do PowerShell e some ao fechá-la.

## Segurança

- Os scripts não usam `shell=True`, então os parâmetros não podem ser usados para injetar comandos.
- Os arquivos `.sql` e a pasta `backups/` estão no `.gitignore`, para não irem para o GitHub por engano.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
