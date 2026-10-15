import sys
from src.lib.text import normalize, tokenize, count_freq, top_n

if __name__ == "__main__":
    # Считываем весь многострочный текст из стандартного ввода до символа EOF
    stdin_text = sys.stdin.read()

    normalized_text = normalize(stdin_text)
    tokens = tokenize(normalized_text)
    frequencies = count_freq(tokens)
    top_words = top_n(frequencies, n=5)

    print(f'Всего слов: {len(tokens)}')
    print(f'Уникальных слов: {len(frequencies)}')
    print('Топ-5:')
    for word, count in top_words:
        print(f'{word}:{count}')