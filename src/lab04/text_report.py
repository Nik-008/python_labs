import sys
from src.lab04.io_txt_csv import read_text, write_csv
from src.lib.text import count_freq, normalize, tokenize, top_n

def main() -> None:
    input_path = "data/input.txt"
    output_path = "data/report.csv"

    try:
        text = read_text(input_path, encoding="utf-8")
    except FileNotFoundError:
        print(f"Ошибка: Входной файл не найден по пути: {input_path}")
        sys.exit(1)

    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    frequencies = count_freq(tokens)
    sorted_rows = sorted(frequencies.items(), key=lambda kv: (-kv[1], kv[0]))

    write_csv(sorted_rows, output_path, header=("word", "count"))
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(frequencies)}")
    print("Топ-5:")
    for word, count in top_n(frequencies, 5):
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()