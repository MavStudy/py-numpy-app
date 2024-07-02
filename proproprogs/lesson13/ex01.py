# NumPy - Транслирование массивов
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
    # Представьте, что у нас имеются два массива с разным числом элементов:
    a = np.array([1, 2, 3, 10, 20, 30])
    array_info('a', a)
    print(a)
    # массив a: <class 'numpy.ndarray'> 5681488 (6,)
    # [ 1  2  3 10 20 30]

    separator()

    b = np.array([2])
    array_info('b', b)
    print(b)
    # массив b: <class 'numpy.ndarray'> 32726064 (1,)
    # [2]

    separator()

    # Можем ли мы выполнять арифметические операции с такими объектами?
    # Оказывается да, можем, например:
    print(a * b)
    # [ 2  4  6 20 40 60]

    separator()

    print(a + b)
    # [ 3  4  5 12 22 32]

    separator()

    # В первом случае каждый элемент массива a будет умножен на первый элемент
    # массива b. А во втором случае выполняется аналогичная операция сложения.
    # Но почему это сработало? Например, если мы в массиве b пропишем два
    # элемента:
    b = np.array([2, 3])
    array_info('b', b)
    print(b)
    # массив b: <class 'numpy.ndarray'> 161761680 (2,)
    # [2 3]

    separator()

    # и выполним ту же операцию умножения:
    #
    # print(a * b)  # ошибка, размеры не согласованы
    #
    # ValueError: operands could not be broadcast together
    # with shapes (6,) (2,)

    # возникнет ошибка. Так почему в первом случае это сработало,
    # а во втором – не сработало? Все дело в особенностях работы алгоритма
    # транслирования массивов пакета NumPy, который следует двум правилам:
    #
    # 1. Если массивы имеют разное число осей (размерностей), то к массиву
    # с меньшим их числом добавляются новые так, чтобы размерности совпадали.
    # (Причем, добавление всегда происходит с оси axis0).
    #
    # 2. Оси с одним элементом расширяются (по числу элементов) так,
    # чтобы соответствующие размерности двух массивов совпадали.

    # Чтобы все было понятнее, давайте рассмотрим эти правила на конкретных
    # примерах. Если обратиться к массивам a и b, то число осей у них
    # одинаковое. В этом легко убедиться, выполнив команды:

    print(a.ndim)  # 1
    print(b.ndim)  # 1

    separator()

    # То есть, первый пункт выполняется. И, когда массив b содержал всего один
    # элемент, то согласно второму пункту он мог размножиться до размеров
    # массива a. Получаем равные массивы а, значит, с ними можно выполнять
    # любые математические операции.

    # Соответственно, как только в массив b был добавлен еще один второй
    # элемент, то второй пункт не мог быть реализован, и возникла ошибка при
    # вычислении.


if __name__ == '__main__':
    main()
