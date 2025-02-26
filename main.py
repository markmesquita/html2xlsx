import sys
from html_to_excel import convert_html_to_excel
from utils import print_help

if __name__ == "__main__":
    # Verifica se o usuário pediu a ajuda
    if len(sys.argv) == 2 and sys.argv[1] in ["--help", "-h"]:
        print_help()

    # Verifica se os argumentos foram passados corretamente
    if len(sys.argv) < 3:
        print("❌ Erro: Argumentos insuficientes!")
        print("🔹 Use --help para mais informações.")
        sys.exit(1)

    html_file = sys.argv[1]
    excel_file = sys.argv[2]

    convert_html_to_excel(html_file, excel_file)
