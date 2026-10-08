def transpose(mat: list[list[float | int]]) -> list[list]:
    """Транспонирует прямоугольную матрицу."""

    if len(mat) == 0: return []
    etalon = len(mat[0])
    for row in mat:
        if len(row) != etalon:
            raise ValueError("Строки разной длины")

    rows = len(mat)
    cols = len(mat[0])

    result = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = mat[i][j]
    return result


def row_sums(mat: list[list[float | int]]) -> list[float]:
    """Возвращает список сумм элементов по каждой строке прямоугольной матрицы."""

    if len(mat) == 0: return []
    etalon = len(mat[0])
    for row in mat:
        if len(row) != etalon:
            raise ValueError("Строки разной длины")

    result = []

    for row in mat:
        row_sum = 0
        for element in row:
            row_sum += element
        result.append(row_sum)
    return result


def col_sums(mat: list[list[float | int]]) -> list[float]:
    """Возвращает список сумм элементов по каждому столбцу матрицы."""

    if len(mat) == 0: return []
    etalon = len(mat[0])
    for row in mat:
        if len(row) != etalon:
            raise ValueError("Строки разной длины")

    rows = len(mat)
    cols = len(mat[0])

    result = [0] * cols
    
    for j in range(cols):
        for i in range(rows):
            result[j] += mat[i][j]
    return result


if __name__ == "__main__":
    #Тестирование функции transpose
    print(transpose([[1, 2, 3]]))
    print(transpose([[1], [2], [3]]))
    print(transpose([[1, 2], [3, 4]]))
    print(transpose([]))
    try:
        print(transpose([[1, 2], [3]]))
    except ValueError:
        print("ValueError")

    print()

    #Тестирование функции row_sums
    print(row_sums([[1, 2, 3], [4, 5, 6]]))
    print(row_sums([[-1, 1], [10, -10]]))
    print(row_sums([[0, 0], [0, 0]]))
    try:
        print(row_sums([[1, 2], [3]]))
    except ValueError:
        print("ValueError")

    print()

    #Тестирование функции col_sums
    print(col_sums([[1, 2, 3], [4, 5, 6]]))
    print(col_sums([[-1, 1], [10, -10]]))
    print(col_sums([[0, 0], [0, 0]]))
    try:
        print(col_sums([[1, 2], [3]]))
    except ValueError:
        print("ValueError")