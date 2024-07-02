# ex14.py - Функции формирования массивов на основе данных
import numpy as np


def getRange(x, y):
    return 100 * x + y


def main():
    # Формирование массива с помощью функции выполняется следующим образом:
    a = np.fromfunction(getRange, (2, 2))
    print(a)

    # Часто совместно с fromfunction используют лямбда-функции в виде:
    b = np.fromfunction(lambda x, y: x * 100 + y, (2, 2))
    print(b)


if __name__ == '__main__':
    main()
# [[  0.   1.]
#  [100. 101.]]
