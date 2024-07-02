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
    # Тригонометрические функции
    #
    # Конечно, любой состоятельный математический пакет должен иметь в своем
    # составе тригонометрические функции и NumPyздесь не исключение. Наиболее
    # употребительные из них приведены в следующей таблице:

    # ------------------------------------------------------------------------
    #  Название     | Описание
    # ------------------------------------------------------------------------
    #  np.sin(x)    | Вычисление синуса угла x (в радианах); xможет быть
    #               | числом, списком, массивом (это правило распространяется
    #               | на все функции этой таблицы).
    # ------------------------------------------------------------------------
    #  np.cos(x)    | Вычисление косинуса угла(ов) x.
    # ------------------------------------------------------------------------
    #  np.tan(x)    | Вычисление тангенса угла(ов) x.
    # ------------------------------------------------------------------------
    #  np.arccos(x) | Арккосинус угла(ов) x.
    # ------------------------------------------------------------------------
    #  np.arcsin(x) | Арксинус угла(ов) x.
    # ------------------------------------------------------------------------
    #  np.arctan(x) | Арктангенс угла(ов) x.
    # ------------------------------------------------------------------------

    # Предположим, имеется массив:
    a = np.linspace(0, np.pi, 10)

    array_info('a', a)
    print(a)
    # массив a: <class 'numpy.ndarray'> 42865552 (10,)
    # [0.         0.34906585 0.6981317  1.04719755 1.3962634  1.74532925
    #  2.0943951  2.44346095 2.7925268  3.14159265]
    separator()

    res1 = np.sin(a)  # возвращает массив синусов углов
    print(res1)
    # [0.00000000e+00 3.42020143e-01 6.42787610e-01 8.66025404e-01
    #  9.84807753e-01 9.84807753e-01 8.66025404e-01 6.42787610e-01
    #  3.42020143e-01 1.22464680e-16]
    separator()

    print(f"{np.sin(np.pi/3) = }")
    # np.sin(np.pi/3) = 0.8660254037844386
    separator()

    print(np.cos([0, 1.57, 3.17]))
    # [ 1.00000000e+00  7.96326711e-04 -9.99596538e-01]
    separator()

    res2 = np.cos(a)  # возвращает массив косинусов углов
    print(res2)
    # [ 1.          0.93969262  0.76604444  0.5         0.17364818 -0.17364818
    #   -0.5        -0.76604444 -0.93969262 -1.        ]
    separator()

    print(np.arcsin(res1))  # возвращает арксинусы от значений res1
    # [0.00000000e+00 3.49065850e-01 6.98131701e-01 1.04719755e+00
    #  1.39626340e+00 1.39626340e+00 1.04719755e+00 6.98131701e-01
    #  3.49065850e-01 1.22464680e-16]
    separator()

    # Причем, все эти функции работают быстрее аналогичных функций
    # языка Python. Поэтому, при использовании библиотеки NumPy предпочтение
    # лучше отдавать именно ей, а не языку Python при тригонометрических
    # вычислениях.


if __name__ == '__main__':
    main()