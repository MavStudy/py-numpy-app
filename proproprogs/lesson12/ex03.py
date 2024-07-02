# NumPy - Множества (unique) и операции над ними
import numpy as np


def separator(sep='-'):
    print(sep * 70)


def array_info(name, arr):
    print(
        f"массив {name}:",
        type(arr),
        id(arr),
        arr.shape
    )


def main():
    # Операции над множествами.
    # В NumPy есть несколько функций для выполнения базовых операций
    # с множествами. Первая – это проверка вхождений элементов одного
    # множества в другое. Например, заданы два массива с уникальными
    # значениями (множества):
    x = np.array([0, 1, 2, 3])
    array_info('x', x)
    print(x)
    # массив x: <class 'numpy.ndarray'> 1791966633520 (4,)
    # [0 1 2 3]
    separator()
    y = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    array_info('y', y)
    print(y)
    # массив y: <class 'numpy.ndarray'> 1792108797488 (8,)
    # [1 2 3 4 5 6 7 8]
    separator()

    print(np.in1d(x, y))
    # [False  True  True  True]

    # На выходе получим массив булевых значений и там где стоит False означает
    # отсутствие элемента, а там где стоит True – наличие совпадения. Причем,
    # порядок следования элементов не имеет никакого значения.

    separator()

    # Если перемешать массив y:
    np.random.shuffle(y)
    array_info('y', y)
    print(y)
    # массив y: <class 'numpy.ndarray'> 1929949355568 (8,)
    # [8 2 6 1 5 3 7 4]

    separator()

    print(np.in1d(x, y))
    # [False  True  True  True]


if __name__ == '__main__':
    main()
