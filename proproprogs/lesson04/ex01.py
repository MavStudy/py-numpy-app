# Свойства и представления массивов, создание их копий
import numpy as np


def main():
    a1 = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
    print(id(a1), a1.dtype, a1.size, a1.itemsize)
    print(a1.size * a1.itemsize)
    print(a1)

    print('-' * 30)

    a1.dtype = np.int8()
    print(id(a1), a1.dtype, a1.size, a1.itemsize)
    print(a1.size * a1.itemsize)
    print(a1)

    print('-' * 30)

    a1.dtype = 'float32'
    print(id(a1), a1.dtype, a1.size, a1.itemsize)
    print(a1.size * a1.itemsize)
    print(a1)


if __name__ == '__main__':
    main()
