# Изменение формы массивов, добавление и удаление осей
import numpy as np


def main():
    # Транспонирование матриц и векторов

    # Очень часто в математических операциях требуется выполнять
    # транспонирование матриц и векторов, то есть, заменять строки на столбцы.
    # Например, если имеется матрица (двумерный массив):
    a = np.array([(1, 2, 3), (1, 4, 9), (1, 8, 27)])
    print(
        "a - первоначальное представление массива",
        id(a),
        a.shape
    )
    print(a)

    print('-' * 70)

    # то операция транспонирования может быть реализована так:
    b = a.T

    # Обратите внимание, мы здесь создаем лишь новое представление тех же самых
    # данных массива a.
    print(
        "b - транспонированное представление массива",
        id(b),
        b.shape
    )
    print(b)

    print('-' * 70)

    # И изменение элементов в массиве b:
    b[0, 1] = 10  # приведет к соответствующему изменению значения элемента
    # и массива a. Это следует помнить, используя операцию транспонирования.
    print(
        "a - первоначальное представление массива",
        id(a),
        a.shape
    )
    print(a)

    print('-' * 70)

    print(
        "b - транспонированное представление массива",
        id(b),
        b.shape
    )
    print(b)


if __name__ == '__main__':
    main()