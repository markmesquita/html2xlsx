import sys
from html_to_excel import convert_html_to_excel
from utils import print_help

if __name__ == "__main__":
    # Check if the user asked for help
    if len(sys.argv) == 2 and sys.argv[1] in ["--help", "-h"]:
        print_help()

    # Check if the arguments were passed correctly
    if len(sys.argv) < 3:
        print("❌ Error: Insufficient arguments!")
        print("🔹 Use --help for more information.")
        sys.exit(1)

    html_file = sys.argv[1]
    excel_file = sys.argv[2]

    convert_html_to_excel(html_file, excel_file)
