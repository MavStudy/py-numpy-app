# NumPy - Базовые математические функции
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
    # Функции математической статистики
    #
    # Последняя группа общематематических функций, которую мы рассмотрим на этом
    # занятии, отвечает за вычисления статистических характеристик случайных
    # величин. Основные из них, следующие:
    #
    # --------------------------------------------------------------------------
    # Название          | Описание
    # --------------------------------------------------------------------------
    # np.median(x)      | Вычисление медианы величин x
    # --------------------------------------------------------------------------
    # np.var(x)         | Дисперсия величин x
    # --------------------------------------------------------------------------
    # np.std(x)         | Среднеквадратическое отклонение величин x
    # --------------------------------------------------------------------------
    # np.corrcoef(x)    | Линейный коэффициент корреляции Пирсона
    # --------------------------------------------------------------------------
    # np.correlate(x)   | Вычисление кросс-корреляции
    # --------------------------------------------------------------------------
    # np.cov(x)         | Вычисление ковариационной матрицы
    # --------------------------------------------------------------------------

    # Рассмотрим работу этих функций. Предположим, имеются следующие векторы:
    x = np.array([1, 4, 3, 7, 10, 8, 14, 21, 20, 23])
    y = np.array([4, 1, 6, 9, 13, 11, 16, 19, 15, 22])

    # Эти числа будем воспринимать как реализации случайных величин X и Y.
    # Тогда, для вычисления медианы СВХ, можно воспользоваться функцией:
    print(np.median(x))  # 9.0

    separator()

    # Для расчёта дисперсии и СКО, функциями:
    print(np.var(x))  # дисперсия СВХ на основе реализации x
    # 57.29

    separator()

    print(np.std(y))  # СКО CBY на основе реализации y
    # 6.359245238233859

    separator()

    # Далее, чтобы рассчитать коэффициент корреляции Пирсона,
    # объединим массивыx и y построчно:
    XY = np.vstack([x, y])  # матрица 2х10
    array_info('XY', XY)
    print(XY)
    # массив XY: <class 'numpy.ndarray'> 2914454085360 (2, 10)
    # [[ 1  4  3  7 10  8 14 21 20 23]
    #  [ 4  1  6  9 13 11 16 19 15 22]]

    separator()

    print(np.corrcoef(XY))
    # [[1.         0.93158099]
    #  [0.93158099 1.        ]]

    # Как ее следует интерпретировать? В действительности,
    # это автоковариационная матрица вектора СВ[X, Y]

    # см. автоковариационная_матрица.png

    # (В этой формуле полагается, что СВX и Y центрированы,
    # то есть имеют нулевое математическое ожидание).
    #
    # Если нужно вычислить не нормированное МО, то есть, автоковариационную
    # матрицу, то следует воспользоваться функцией:

    print(np.cov(XY))  # ковариационная матрица размерностью 2х2
    # [[1.         0.93158099]
    #  [0.93158099 1.        ]]
    # [[63.65555556 49.82222222]
    #  [49.82222222 44.93333333]]

    separator()

    # Наконец, для вычисления взаимной корреляции между двумя векторами x и y,
    # используется функция:
    print(np.correlate(x, y))  # array([1736])
    # [1736]

    separator()

    # Более детальную информацию по этим статистическим функциям можно найти
    # в официальной документации пакета NumPy:
    #
    # https://numpy.org/doc/stable/


if __name__ == '__main__':
    main()
