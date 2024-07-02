# Функции формирования числовых диапазонов
import numpy as np


def main():
    # Похожим образом работает и функция linspace. Она разбивает указанный
    # интервал на равномерные отрезки и возвращает массив этих значений.

    # Мы указываем в качестве аргументов интервал [start; stop] и число
    # отметок в этом интервале n. Если n = 0, то получим пустой массив.
    # При n = 1 – значение start. При n = 2 – значения start и stop.
    # При n> 2 равномерное разбиение интервала точками m = n-2.
    # Например:

    a1 = np.linspace(0, np.pi, 0)  # пустой массив
    print(a1)
    a2 = np.linspace(0, np.pi, 1)  # одно значение 0
    print(a2)
    a3 = np.linspace(0, np.pi, 2)  # два значения: 0 и pi
    print(a3)
    a4 = np.linspace(0, np.pi, 3)  # три значения: 0, pi/2, pi
    print(a4)
    # В чем отличие linspace от arange? В arange мы указываем сами шаг
    # движения по числовой оси. При этом число значений определяется
    # граничными значениями. А в linspace мы задаем граничные значения
    # и число делений, а шаг вычисляется автоматически.


if __name__ == '__main__':
    main()
# []
# [0.]
# [0.         3.14159265]
# [0.         1.57079633 3.14159265]