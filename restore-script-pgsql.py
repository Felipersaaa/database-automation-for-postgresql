#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description="Restauração de backup PostgreSQL")
    parser.add_argument("--host", required=True, help="Host do PostgreSQL")
    parser.add_argument("--db", required=True, help="Nome do banco de destino")
    parser.add_argument("--file", required=True, help="Arquivo .sql de backup")
    parser.add_argument("--user", default="postgres", help="Usuário (padrão: postgres)")
    parser.add_argument("--port", default="5432", help="Porta (padrão: 5432)")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Erro: o arquivo {args.file} não existe.")
        sys.exit(1)

    restore_command = [
        "psql",
        "-h", args.host,
        "-p", str(args.port),
        "-U", args.user,
        "-d", args.db,
        "-f", args.file,
    ]

    try:
        subprocess.run(restore_command, check=True)
    except FileNotFoundError:
        print("Erro: o comando psql não foi encontrado.")
        print("Instale o PostgreSQL e confira se o psql está disponível no terminal.")
        sys.exit(1)
    except subprocess.CalledProcessError as erro:
        print(f"Erro: a restauração falhou (código {erro.returncode}).")
        sys.exit(1)

    print(f"Restauração concluída no banco: {args.db}")


if __name__ == "__main__":
    main()
