import csv
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Читает файл целиком в одну строку. По умолчанию кодировка UTF-8.

    Если нужно прочитать файл в кодировке Windows, вызывайте так:
    read_text("data/input.txt", encoding="cp1251")

    """
    
    p = Path(path)
    return p.read_text(encoding=encoding)


def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """
    Создает или перезаписывает CSV-файл с разделителем-запятой.

    Если передан header, он записывается первой строкой.
    Если строки в rows имеют разную длину, вызывается ошибка ValueError.

    """
    
    p = Path(path)

    if len(rows) > 0:
        etalon_len = len(rows[0])
        for row in rows:
            if len(row) != etalon_len:
                raise ValueError("Все строки в rows должны иметь одинаковую длину!")

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)