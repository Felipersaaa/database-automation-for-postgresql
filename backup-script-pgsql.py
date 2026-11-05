#!/usr/bin/env python3

import subprocess
import argparse
import os
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="Backup automático de PostgreSQL")
    parser.add_argument("--host", required=True, help="Host do PostgreSQL")
    parser.add_argument("--db", required=True, help="Nome do banco")
    parser.add_argument("--output", required=True, help="Pasta de saída")
    args = parser.parse_args()

    # Crie a pasta de backup se não existir
    if not os.path.exists(args.output):
        os.makedirs(args.output)

    # Comando para fazer backup do PostgreSQL
    backup_command = f"pg_dump -h {args.host} -U postgres {args.db} > {args.output}/backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.sql"
    subprocess.run(backup_command, shell=True, check=True)

    print("Backup realizado com sucesso!")

if __name__ == "__main__":
    main()

