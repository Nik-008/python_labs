import csv
from pathlib import Path
from openpyxl import Workbook

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Для конвертации используется библиотека openpyxl.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".

    """

    c_p = Path(csv_path)
    x_p = Path(xlsx_path)
    
    if not c_p.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")
        
    with c_p.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)
        
    if len(rows) == 0:
        raise ValueError("Неверный тип файла, пустой JSON или CSV")
        
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    
    for row in rows:
        ws.append(row)
        
    x_p.parent.mkdir(parents=True, exist_ok=True)
    wb.save(x_p)

if __name__ == '__main__':
    csv_to_xlsx('data/lab05/samples/cities.csv', 'data/lab05/out/people.xlsx')