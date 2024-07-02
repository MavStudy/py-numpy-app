# ex13.py - Функции формирования массивов на основе данных
import numpy as np


def main():
    # Функция copy выполняет копирование массива.
    a1 = np.array([(1, 2), (3, 4)])
    b1 = np.copy(a1)
    print(id(a1))
    print(a1)
    print(id(b1))
    print(b1)
    # 32049744
    # [[1 2]
    #  [3 4]]
    # 32050224
    # [[1 2]
    #  [3 4]]


if __name__ == '__main__':
    main()
