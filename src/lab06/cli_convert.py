import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("json2csv", help="Преобразует .json в .csv")
    p1.add_argument("--in", dest="input", required=True, help="Входной файл .json")
    p1.add_argument("--out", dest="output", required=True, help="Выходной файл .csv")

    p2 = sub.add_parser("csv2json", help="Преобразует .csv в .json")
    p2.add_argument("--in", dest="input", required=True, help="Входной файл .csv")
    p2.add_argument("--out", dest="output", required=True, help="Выходной файл .json")

    p3 = sub.add_parser("csv2xlsx", help="Преобразует .csv в .xlsx")
    p3.add_argument("--in", dest="input", required=True, help="Входной файл .csv")
    p3.add_argument("--out", dest="output", required=True, help="Выходной файл .xlsx")

    args = parser.parse_args()

    try:
        if args.cmd == "json2csv":
            json_to_csv(args.input, args.output)
        elif args.cmd == "csv2json":
            csv_to_json(args.input, args.output)
        elif args.cmd == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
    except FileNotFoundError:
        parser.error(f"файл не найден: {args.input}")
    except ValueError as e:
        parser.error(str(e))


if __name__ == "__main__":
    main()