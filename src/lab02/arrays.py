def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """Возвращает (минимум, максимум) из списка чисел."""

    if len(nums) == 0: raise ValueError("Список пуст")

    mn, mx = nums[0], nums[0]
    for num in nums[1:]:
        if num < mn: mn = num
        if num > mx: mx = num
    return mn, mx


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """Возвращает отсортированный список уникальных значений по возрастанию."""

    if len(nums) == 0: return []

    unique_nums = list(set(nums))

    ln = len(unique_nums)
    for i in range(ln):
        for j in range(0, ln-i-1):
            if unique_nums[j] > unique_nums[j + 1]:
                unique_nums[j], unique_nums[j + 1] = unique_nums[j + 1], unique_nums[j]
    return unique_nums


def flatten(mat: list[list | tuple]) -> list:
    """«Расплющивает» список списков или кортежей в один плоский список."""

    result = []

    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError("Элементы матрицы должны быть списками или кортежами")
        for element in row:
            result.append(element)
    return result


if __name__ == "__main__":
    #Тестирование функции min_max
    print(min_max([3, -1, 5, 5, 0]))
    print(min_max([42]))
    print(min_max([-5, -2, -9]))
    print(min_max([1.5, 2, 2.0, -3.1]))
    try:
        print(min_max([]))
    except ValueError:
        print("ValueError")

    print()

    #Тестирование функции unique_sorted
    print(unique_sorted([3, 1, 2, 1, 3]))
    print(unique_sorted([]))
    print(unique_sorted([-1, -1, 0, 2, 2]))
    print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

    print()

    #Тестирование функции flatten
    print(flatten([[1, 2], [3, 4]]))
    print(flatten([[1, 2], (3, 4, 5)]))
    print(flatten([[1], [], [2, 3]]))
    try:
        print(flatten([[1, 2], "ab"]))
    except TypeError:
        print("TypeError")