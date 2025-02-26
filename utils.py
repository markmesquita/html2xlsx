import sys

def print_help():
    """Exibe as informações de ajuda sobre o uso da aplicação"""
    help_text = """
📌 Conversor de HTML para Excel

Este script converte um arquivo do tipo HTML contendo parâmetros de pesquisa e tabelas em um arquivo Excel (.xlsx).

🔹 Uso:
    python main.py <arquivo_entrada> <arquivo_saida.xlsx>

🔹 Exemplo:
    python main.py relatorio.html relatorio.xlsx

🔹 Opções:
    --help       Exibe esta mensagem de ajuda e sai.

🔹 Instalação:
    Antes de executar o script, instale as dependências do Python.

    🖥️ Windows:
        1️⃣ Instale o Python: https://www.python.org/downloads/
        2️⃣ Abra o terminal (cmd ou PowerShell)
        3️⃣ Execute:
            pip install openpyxl lxml tqdm

    🐧 Linux (Ubuntu, Debian e outros):
        1️⃣ Instale o Python e dependências:
            sudo apt update && sudo apt install python3 python3-pip -y
        2️⃣ Execute:
            pip install openpyxl lxml tqdm

    🍏 macOS:
        1️⃣ Instale o Python (se não tiver):
            brew install python3
        2️⃣ Execute:
            pip install openpyxl lxml tqdm

🔹 Dependências:
    - openpyxl  (para criar arquivos Excel)
    - lxml      (para processar HTML)
    - tqdm      (para exibir barra de progresso)

🔥 Desenvolvido para facilitar a extração de dados de relatórios HTML para Excel!
"""
    print(help_text)
    sys.exit(0)
