def task1():
    print("=== ЗАДАЧА 1 ===")
    print("Поиск максимального элемента массива и его порядкового номера")
    try:
        arr = list(map(int, input("Введите целые числа через пробел: ").split()))
        if not arr:
            print("Массив пуст!")
            return
    except ValueError:
        print("Ошибка! Введите только целые числа.")
        return
    max_element = arr[0]
    max_index = 0
    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
            max_index = i
    print(f"Массив: {arr}")
    print(f"Максимальный элемент: {max_element}")
    print(f"Порядковый номер (с 1): {max_index + 1}")
    print(f"Индекс (с 0): {max_index}")

def task2():
    print("\n=== ЗАДАЧА 2 ===")
    print("Получение массива нечетных чисел в порядке убывания")
    try:
        arr = list(map(int, input("Введите целые числа через пробел: ").split()))
    except ValueError:
        print("Ошибка! Введите только целые числа.")
        return
    odd_numbers = [x for x in arr if x % 2 != 0]
    if not odd_numbers:
        print("В исходном массиве нет нечетных чисел.")
    else:
        odd_numbers.sort(reverse=True)
        print(f"Исходный массив: {arr}")
        print(f"Массив нечетных чисел (по убыванию): {odd_numbers}")

def main():
    print("ПРОГРАММА ДЛЯ РАБОТЫ С МАССИВАМИ")
    print("=" * 40)
    while True:
        print("\nВыберите задачу:")
        print("1 - Найти максимальный элемент и его порядковый номер")
        print("2 - Получить массив нечетных чисел в порядке убывания")
        print("3 - Выполнить обе задачи")
        print("0 - Выход")
        choice = input("Ваш выбор: ")
        if choice == '1':
            task1()
        elif choice == '2':
            task2()
        elif choice == '3':
            task1()
            task2()
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")

if __name__ == "__main__":
    main()