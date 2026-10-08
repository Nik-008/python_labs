def format_record(rec: tuple[str, str, float]) -> str:
    """Форматирует запись о студенте, собирая инициалы и округляя GPA."""

    # 1. Проверка типов данных (TypeError)
    if not isinstance(rec, tuple) or len(rec) != 3:
        raise TypeError("Входные данные должны быть кортежем из 3 элементов")

    fio, group, gpa = rec

    if not isinstance(fio, str) or not isinstance(group, str):
        raise TypeError("ФИО и Группа должны быть строками")
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должен быть числом")

    # 2. Проверка корректности значений (ValueError)
    if not fio.strip() or not group.strip():
        raise ValueError("ФИО и Группа не могут быть пустыми строками")
    if not (0.0 <= gpa <= 5.0):
        raise ValueError("GPA должен быть в диапазоне от 0.0 до 5.0")

    words = fio.split()
    if len(words) < 2:
        raise ValueError("ФИО должно содержать как минимум Фамилию и Имя")

    # 3. Сборка фамилии и инициалов
    last_name = words[0].capitalize()
    initials = f"{words[1][0].upper()}."
    if len(words) >= 3:
        initials += f"{words[2][0].upper()}."

    return f"{last_name} {initials}, гр. {group.strip()}, GPA {gpa:.2f}"


if __name__ == "__main__":
    #Тестирование format_record
    print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
    print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
    print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
    print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
    try:
        print(format_record(("", "BIVT-25", 4.6)))
    except ValueError:
        print("ValueError")
    try:
        print(format_record(("Иванов Иван Иванович", "", 4.6)))
    except ValueError:
        print("ValueError")
    try:
        print(format_record(("Иванов Иван Иванович", "BIVT-25", -1.0)))
    except ValueError:
        print("ValueError")