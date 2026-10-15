import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    Выполняет нормализацию текста:
    приводит к нижнему регистру, заменяет ё на е, убирает управляющие символы, обрезает края и схлопывает пробелы.

    """

    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace('ё','е')

    text = text.replace('\t',' ').replace('\r',' ').replace('\n',' ')

    text = text.strip()
    return ' '.join(text.split())


def tokenize(text: str) -> list[str]:
    """Разбивает текст на список слов (токенов), сохраняя дефисы внутри слов."""

    return re.findall(r'\w+(?:-\w+)*', text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Подсчитывает частоту встречаемости каждого слова в списке."""

    freq = {}
    for w in tokens:
        freq[w] = freq.get(w, 0) + 1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    Возвращает список из N самых часто встречающихся слов.
    Сортировка выполняется сначала по убыванию частоты слова,
    а при равных частотах - по алфавиту.

    """

    pairs = sorted(freq.items(), key = lambda p: (-p[1], p[0]))
    return pairs[:n]


if __name__ == "__main__":
    # Тестирование normalize
    print(normalize("ПрИвЕт\nМИр\t"))
    print(normalize("ёжик, Ёлка"))
    print(normalize("Hello\r\nWorld"))
    print(normalize("  двойные   пробелы  "))

    print()

    # Тестирование tokenize
    print(tokenize("привет мир"))
    print(tokenize("hello,world!!!"))
    print(tokenize("по-настоящему круто"))
    print(tokenize("2025 год"))
    print(tokenize("emoji 😀 не слово"))

    print()

    # Тестирование count_freq + top_n
    freq1 = count_freq(["a","b","a","c","b","a"])
    print(freq1)
    print(top_n(freq1, n=2))
    freq2 = count_freq(["bb","aa","bb","aa","cc"])
    print(freq2)
    print(top_n(freq2, n=2))