import os
import openpyxl
from lxml import etree
from tqdm import tqdm

def extract_html_data(html_file):
    """Extrai parâmetros da pesquisa e dados da tabela do HTML"""
    with open(html_file, "r", encoding="utf-8") as f:
        parser = etree.HTMLParser()
        tree = etree.parse(f, parser)

    data = []

    # 📌 1️⃣ Extraindo Parâmetros de Pesquisa (Divs + Listas sem duplicação)
    params_section = tree.xpath("//div[@class='agr-parametros']")
    if params_section:
        data.append(["Parâmetros de Pesquisa"])  # Cabeçalho
        param_rows = []

        for ul in params_section[0].xpath(".//ul"):
            for li in ul.xpath("./li"):
                strong = li.xpath("./strong/text()")  # Captura o nome do parâmetro
                value = li.xpath("./text()")  # Captura o valor do parâmetro

                strong_text = strong[0].strip() if strong else ""
                value_text = value[0].strip() if value else "-"

                if strong_text:
                    param_rows.append([strong_text, value_text])  # Adiciona o par chave-valor

        data.extend(param_rows)
        data.append([])  # Linha em branco para separar da tabela

    # 📌 2️⃣ Extraindo Dados da Tabela
    table = tree.xpath("//table")
    if table:
        rows = table[0].xpath(".//tr")  # Obtém todas as linhas da tabela
        for row in tqdm(rows, desc="🔍 Processando HTML", unit="linha"):
            row_data = []
            for cell in row.xpath(".//th | .//td"):
                text = "".join(cell.xpath(".//text()")).strip()
                row_data.append(text)
            data.append(row_data)

    return data

def create_excel_file(data, filename):
    """Cria um arquivo Excel a partir dos dados extraídos"""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Relatório"

    for row in tqdm(data, desc="📊 Criando Excel", unit="linha"):
        ws.append(row)

    for col in ws.columns:
        max_length = 0
        col_letter = openpyxl.utils.get_column_letter(col[0].column)
        for cell in col:
            try:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))
            except:
                pass
        ws.column_dimensions[col_letter].width = max_length + 2  # Adiciona margem

    wb.save(filename)
    print(f"✅ Arquivo Excel salvo como: {filename}")

def convert_html_to_excel(html_file, output_excel):
    """Função principal que lê o HTML e gera o Excel"""
    if not os.path.exists(html_file):
        print(f"❌ Erro: Arquivo '{html_file}' não encontrado!")
        return
    
    print(f"🔍 Lendo o arquivo HTML: {html_file}")
    table_data = extract_html_data(html_file)

    print(f"📊 Criando o arquivo Excel: {output_excel}")
    create_excel_file(table_data, output_excel)

    print("✅ Conversão concluída!")
