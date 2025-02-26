import os
import openpyxl
from lxml import etree
from tqdm import tqdm

def extract_html_data(html_file):
    """Extracts search parameters and table data from the HTML file"""
    with open(html_file, "r", encoding="utf-8") as f:
        parser = etree.HTMLParser()
        tree = etree.parse(f, parser)

    data = []

    # 📌 1️⃣ Extracting Search Parameters (Divs + Lists without duplication)
    params_section = tree.xpath("//div[@class='agr-parametros']")
    if params_section:
        data.append(["Search Parameters"])  # Header
        param_rows = []

        for ul in params_section[0].xpath(".//ul"):
            for li in ul.xpath("./li"):
                strong = li.xpath("./strong/text()")  # Get the parameter name
                value = li.xpath("./text()")  # Get the parameter value

                strong_text = strong[0].strip() if strong else ""
                value_text = value[0].strip() if value else "-"

                if strong_text:
                    param_rows.append([strong_text, value_text])  # Add key-value pair

        data.extend(param_rows)
        data.append([])  # Blank row to separate from the table

    # 📌 2️⃣ Extracting Table Data
    table = tree.xpath("//table")
    if table:
        rows = table[0].xpath(".//tr")  # Get all table rows
        for row in tqdm(rows, desc="🔍 Processing HTML", unit="row"):
            row_data = []
            for cell in row.xpath(".//th | .//td"):
                text = "".join(cell.xpath(".//text()")).strip()
                row_data.append(text)
            data.append(row_data)

    return data

def create_excel_file(data, filename):
    """Creates an Excel file from extracted data"""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Report"

    for row in tqdm(data, desc="📊 Creating Excel", unit="row"):
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
        ws.column_dimensions[col_letter].width = max_length + 2  # Add margin

    wb.save(filename)
    print(f"✅ Excel file saved as: {filename}")

def convert_html_to_excel(html_file, output_excel):
    """Main function that reads the HTML and generates the Excel file"""
    if not os.path.exists(html_file):
        print(f"❌ Error: File '{html_file}' not found!")
        return
    
    print(f"🔍 Reading HTML file: {html_file}")
    table_data = extract_html_data(html_file)

    print(f"📊 Creating Excel file: {output_excel}")
    create_excel_file(table_data, output_excel)

    print("✅ Conversion completed!")
