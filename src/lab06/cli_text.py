import argparse
from pathlib import Path
from src.lib import text


def cat(input_path, numbered=False):
    file_path = Path(input_path)
    if not file_path.is_file():
        raise FileNotFoundError(f"Файл не найден: {input_path}")

    with file_path.open("r", encoding="utf-8") as f:
        line_number = 1
        for line in f:
            if numbered:
                print(f"{line_number}: {line}", end="")
            else:
                print(line, end="")
            line_number += 1


def stats(input_path, top=5):
    file_path = Path(input_path)
    if not file_path.is_file():
        raise FileNotFoundError(f"Файл не найден: {input_path}")

    with file_path.open("r", encoding="utf-8") as f:
        content = f.read()

    clean_text = text.normalize(content)
    words = text.tokenize(clean_text)
    frequencies = text.count_freq(words)
    top_words = text.top_n(frequencies, n=top)

    print(f"Всего слов: {len(words)}")
    print(f"Уникальных слов: {len(frequencies)}")
    print(f"Топ-{top}:")
    for word, count in top_words:
        print(f"{word}: {count}")


def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты")
    subparsers = parser.add_subparsers(dest="command", required=True)

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Топ N слов")

    args = parser.parse_args()

    if args.command == "stats" and args.top < 1:
        parser.error("--top должен быть положительным числом")

    try:
        if args.command == "cat":
            cat(args.input, args.n)
        elif args.command == "stats":
            stats(args.input, args.top)
    except FileNotFoundError as e:
        parser.error(str(e))
    except UnicodeDecodeError:
        parser.error(f"Файл {args.input} не читается в кодировке UTF-8")


if __name__ == "__main__":
    main()