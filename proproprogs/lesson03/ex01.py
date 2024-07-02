# Функции автозаполнения, создания матриц и числовых диапазовнов
import numpy as np


def main():
    a = np.array([0] * 10)  # массив из 10 нулей
    print(a)

    b = np.array([1] * 15)  # массив их 15 единиц
    print(b)

    c = np.array([x for x in range(10)])  # массив из чисел от 0 до 9
    print(c)


if __name__ == '__main__':
    main()
