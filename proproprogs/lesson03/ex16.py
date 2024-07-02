# ex16.py - Функции формирования массивов на основе данных
# NumPy: https://numpy.org/doc/stable
import numpy as np


def main():
    # Последняя функция, которую мы рассмотрим fromstring позволяет создавать
    # массив из строковых данных, например, так:
    a = np.fromstring('1 2 3', dtype='int16', sep=' ')
    print(a)

    # десь параметр sep определяет разделитель между данными. Если числа следуют
    # через запятую, то это явно нужно указать в разделителе:
    b = np.fromstring('4, 5, 6', dtype='int16', sep=',')
    print(b)


if __name__ == '__main__':
    main()
# [1 2 3]
# [4 5 6]