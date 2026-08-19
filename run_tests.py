#!/usr/bin/env python3
"""
Script para executar testes com diferentes opções de cobertura
"""
import os
import subprocess
import sys


def run_command(cmd, description):
    """Executa um comando e mostra o resultado"""
    print(f"\n{description}")
    print("=" * 50)
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"Erro ao executar: {cmd}")
        return False
    return True


def main():
    """Função principal"""
    print("DevOps Automation - Test Coverage Runner")
    print("=" * 50)

    if len(sys.argv) > 1:
        option = sys.argv[1]
    else:
        print("\nOpções disponíveis:")
        print("1. Testes simples")
        print("2. Testes com cobertura")
        print("3. Testes com cobertura + relatório HTML")
        print("4. Testes com cobertura + relatório XML")
        print("5. Testes completos (HTML + XML + terminal)")

        option = input("\nEscolha uma opção (1-5): ").strip()

    # Verifica se estamos no diretório correto
    if not os.path.exists("main.py"):
        print("Execute este script no diretório raiz do projeto!")
        sys.exit(1)

    success = True

    if option == "1":
        # Testes simples
        success = run_command("pytest -v", "Executando testes simples")

    elif option == "2":
        # Testes com cobertura no terminal
        success = run_command(
            "pytest --cov=. --cov-report=term-missing -v",
            "Executando testes com cobertura",
        )

    elif option == "3":
        # Testes com cobertura + HTML
        success = run_command(
            "pytest --cov=. --cov-report=html --cov-report=term-missing -v",
            "Executando testes com cobertura + relatório HTML",
        )
        if success:
            print("\nRelatório HTML gerado em: htmlcov/index.html")

    elif option == "4":
        # Testes com cobertura + XML
        success = run_command(
            "pytest --cov=. --cov-report=xml --cov-report=term-missing -v",
            "Executando testes com cobertura + relatório XML",
        )
        if success:
            print("\nRelatório XML gerado em: coverage.xml")

    elif option == "5":
        # Testes completos
        success = run_command(
            "pytest --cov=. --cov-report=html --cov-report=xml --cov-report=term-missing -v",
            "Executando testes completos com todos os relatórios",
        )
        if success:
            print("\nRelatórios gerados:")
            print("  - HTML: htmlcov/index.html")
            print("  - XML: coverage.xml")
            print("  - Terminal: exibido acima")

    else:
        print("Opção inválida!")
        sys.exit(1)

    if success:
        print("\nTestes executados com sucesso!")
    else:
        print("\nAlguns testes falharam!")
        sys.exit(1)


if __name__ == "__main__":
    main()
