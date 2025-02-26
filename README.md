# 🔄 HTML to Excel Converter 📊

This project converts **HTML** files containing **search parameters** and **tables** to **Excel (`.xlsx`)** format in an organized and efficient manner. The intention is to convert very large HTML files into smaller XLSX files, making data reading easier.

---

## 🚀 **Features**

✅ Extracts **search parameters** (`div`, `ul`, `li`) from HTML and organizes them in Excel  
✅ Converts **HTML tables** to Excel while maintaining correct alignment  
✅ Processes large files with **progress bar (`tqdm`)**  
✅ **Compatible with Windows, Linux, and macOS**  
✅ **Integrated help** (`--help`) with detailed instructions

---

## 📥 **Installation**

Before running the application, install Python and the dependencies.

### 🔹 **Creating a Virtual Environment (Avoids the "externally-managed-environment" error)**

If you receive an error like **"externally-managed-environment"** when installing packages, it means that Python does not allow direct installation of packages on the system.  
The solution is to create a **virtual environment (`venv`)**.

### 🖥️ **Windows**

1. Install Python: [Download Python](https://www.python.org/downloads/)
2. Open the terminal (**cmd** or **PowerShell**) and run:

```sh
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 🐧 Linux (Ubuntu, Debian, etc.)

1. Install Python and pip:

```sh
sudo apt update && sudo apt install python3 python3-pip -y
```

2. Create and activate a virtual environment:

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 🍏 macOS

1. Install Python (if not already installed):

```sh
brew install python3
```

2. Create and activate a virtual environment:

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 📂 Project Structure

```sh
html-to-excel/
│── main.py          # Main file (executable)
│── html_to_excel.py # Converts HTML to Excel
│── utils.py         # Auxiliary functions (e.g., --help)
│── README.md        # Project documentation
│── requirements.txt # List of dependencies
└── relatorio.html   # Input file (example)
```

## 📌 Usage

After installing the dependencies, run the script by passing the input HTML and output Excel:

```sh
python main.py relatorio.html relatorio.xlsx
```

## 📖 Help

To display detailed instructions, use the --help argument:

```sh
python main.py --help
```

or

```sh
python main.py -h
```

This will display:

```md
📌 HTML to Excel Converter

This script converts an HTML file containing search parameters and tables into an Excel file (.xlsx).

🔹 Usage:
python main.py <input_file.html> <output_file.xlsx>

🔹 Example:
python main.py relatorio.html relatorio.xlsx

🔹 Options:
--help Displays this help message and exits.

🔹 Installation:
Instructions for Windows, Linux, and macOS.
```

## 🛠 Requirements

- Python 3.6+
- Dependencies (installed via requirements.txt):

```sh
pip install -r requirements.txt
```

## 🤝 Contribution

Feel free to contribute!

Fork the repository

1. Create a branch (git checkout -b my-feature)
2. Make your changes and commit (git commit -m "My improvement")
3. Push (git push origin my-feature)
4. Open a Pull Request 🎉

## 📜 License

This project is under the MIT license.

## ✨ Author

Developed by [Mark Mesquita](https://github.com/markmesquita) 🚀
If you liked the project, leave a star ⭐ on the repository!
