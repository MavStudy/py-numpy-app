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
    # Базовые математические функции
    #
    # Все те же самые операции и многие другие можно выполнять через функции
    # пакета NumPy, а не через методы массива. Вот список основных из них:
    #
    # ------------------------------------------------------------------------
    #  Название     | Описание
    # ------------------------------------------------------------------------
    #  np.abs(x)    | Вычисление модуля от аргумента(ов)x; xможет быть
    #               | числом, списком или массивом.
    # ------------------------------------------------------------------------
    #  np.amax(x)   | Нахождение максимального значения от аргумента(ов)x
    # ------------------------------------------------------------------------
    #  np.amin(x)   | Нахождение минимального значения от аргумента(ов)x
    # ------------------------------------------------------------------------
    #  np.argmax(x) | Нахождение индекса максимального значения для x.
    # ------------------------------------------------------------------------
    #  np.argmin(x) | Нахождение индекса минимального значения для x.
    # ------------------------------------------------------------------------
    #  np.around(x) | Округление до ближайшего целого.
    # ------------------------------------------------------------------------
    #  np.mean(x)   | Вычисление среднего значения.
    # ------------------------------------------------------------------------
    #  np.log(x)    | Вычисление натурального логарифма.
    # ------------------------------------------------------------------------
    #  np.log2(x)   | Вычисление логарифма по основанию 2.
    # ------------------------------------------------------------------------
    #  np.log10(x)  | Вычисление логарифма по основанию 10.
    # ------------------------------------------------------------------------

    # Предположим, имеется массив:
    a = np.array([-1, 1, 5, -44, 32, 2])

    array_info('a', a)
    print(a)
    # массив a: <class 'numpy.ndarray'> 5616336 (6,)
    # [ -1   1   5 -44  32   2]
    separator()

    # тогда для вычисления модулей значений его элементов
    # можно записать команду:
    print(np.abs(a))
    # [ 1  1  5 44 32  2]

    # На выходе получаем новый массив с абсолютными величинами.То же самое
    # будет, если на вход подать обычный список значений:
    print(np.abs([-1, 1, 5, -44, 32, ]))

    # или просто число:
    print(np.abs(-10.5))
    # 10.5
    separator()

    # Эти примеры демонстрируют разные типы входных данных:
    # массив, список, число.
    # Все это допустимо использовать в математических функциях.
    #
    # Остальные функции работают по аналогии, например:
    print(f"{np.amax(a) = }")  # 32
    result_log = np.log(a)
    print(result_log)
    # [       nan 0.         1.60943791        nan 3.4657359  0.69314718]
    # ex02.py:77: RuntimeWarning: invalid value encountered in log
    # result_log = np.log(a)

    print(f"{np.around(0.7) = }")  # 1.0
    separator()

    # Функции amin, amax, mean, argmax, argmin, при работе с многомерными
    # матрицами, могут делать вычисления по строго определенной оси.
    # Например:
    a.resize(2, 3)
    array_info('a', a)
    print(a)
    # массив a: <class 'numpy.ndarray'> 30912848 (2, 3)
    # [[ -1   1   5]
    #  [-44  32   2]]
    separator()

    print(np.amax(a, axis=0))
    # [-1 32 5]
    separator()

    print(np.argmax(a, axis=1))
    # [2 1]


if __name__ == '__main__':
    main()
