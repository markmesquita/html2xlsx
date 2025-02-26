import sys

def print_help():
    """Displays help information about the usage of the application"""
    help_text = """
  📌 HTML to Excel Converter

  This script converts an HTML file containing search parameters and tables into an Excel file (.xlsx).

  🔹 Usage:
    python main.py <input_file> <output_file.xlsx>

  🔹 Example:
    python main.py report.html report.xlsx

  🔹 Options:
    --help       Displays this help message and exits.

  🔹 Installation:
    Before running the script, install the Python dependencies.

    🖥️ Windows:
      1️⃣ Install Python: https://www.python.org/downloads/
      2️⃣ Open the terminal (cmd or PowerShell)
      3️⃣ Run:
        pip install openpyxl lxml tqdm

    🐧 Linux (Ubuntu, Debian, and others):
      1️⃣ Install Python and dependencies:
        sudo apt update && sudo apt install python3 python3-pip -y
      2️⃣ Run:
        pip install openpyxl lxml tqdm

    🍏 macOS:
      1️⃣ Install Python (if not already installed):
        brew install python3
      2️⃣ Run:
        pip install openpyxl lxml tqdm

  🔹 Dependencies:
    - openpyxl  (to create Excel files)
    - lxml      (to process HTML)
    - tqdm      (to display progress bar)

  🔥 Developed to facilitate the extraction of data from HTML reports to Excel!
  """
    print(help_text)
    sys.exit(0)
