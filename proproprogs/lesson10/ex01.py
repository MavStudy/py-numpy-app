# NumPy - Булевы математические функции
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
    # Функции sum, mean, min и max
    #
    # Итак, очень часто на практике требуется вычислять сумму значений
    # элементов массива, их среднее значение, а также находить минимальные
    # и максимальные значения. Для этих целей в NumPy существуют встроенные
    # функции, выполняющие эти действия и сейчас мы посмотрим как они работают.
    # Пусть, как всегда, у нас имеется одномерный массив:
    a = np.array([1, 2, 3, 10, 20, 30])
    array_info('a', a)
    print(a)
    # массив a: <class 'numpy.ndarray'> 4633296 (6,)
    # [ 1  2  3 10 20 30]
    separator()

    # Вычислим сумму, среднее значение и найдем максимальное
    # и минимальное значения:
    print(f"{a.sum() = }")
    print(f"{a.mean() = }")  # среднее значение
    print(f"{a.max() = }")
    print(f"{a.min() = }")
    # a.sum() = 66
    # a.mean() = 11.0
    # a.max() = 30
    # a.min() = 1

    # Как видите, все достаточно просто. Тот же самый результат будет получен
    # и при использовании многомерных массивов. Например:
    a.resize(3, 2)
    array_info('a', a)
    print(a)
    # массив a: <class 'numpy.ndarray'> 5616336 (3, 2)
    # [[ 1  2]
    #  [ 3 10]
    #  [20 30]]
    separator()

    print(f"{a.sum() = }")  # 66
    # a.sum() = 66

    # Но, если требуется вычислить сумму только по какой-то одной оси,
    # то её можно явно указать дополнительным параметром:
    print(a.sum(axis=0))
    # [24 42]
    print(a.sum(axis=1))
    # [ 3 13 50]


if __name__ == '__main__':
    main()