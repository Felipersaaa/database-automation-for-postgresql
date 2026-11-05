#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys
from datetime import datetime


def main():
    parser = argparse.ArgumentParser(description="Backup automático de PostgreSQL")
    parser.add_argument("--host", required=True, help="Host do PostgreSQL")
    parser.add_argument("--db", required=True, help="Nome do banco")
    parser.add_argument("--output", required=True, help="Pasta de saída")
    parser.add_argument("--user", default="postgres", help="Usuário do PostgreSQL (padrão: postgres)")
    parser.add_argument("--port", default="5432", help="Porta do PostgreSQL (padrão: 5432)")
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(args.output, f"backup_{args.db}_{timestamp}.sql")

    backup_command = [
        "pg_dump",
        "-h", args.host,
        "-p", str(args.port),
        "-U", args.user,
        "-d", args.db,
        "-f", backup_file,
    ]

    try:
        subprocess.run(backup_command, check=True)
    except FileNotFoundError:
        print("Erro: o comando pg_dump não foi encontrado.")
        print("Instale o PostgreSQL e confira se o pg_dump está disponível no terminal.")
        sys.exit(1)
    except subprocess.CalledProcessError as erro:
        print(f"Erro: o backup falhou (código {erro.returncode}).")
        if os.path.exists(backup_file):
            os.remove(backup_file)
        sys.exit(1)

    print(f"Backup realizado com sucesso: {backup_file}")


if __name__ == "__main__":
    main()
    
