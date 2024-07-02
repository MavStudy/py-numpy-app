# Свойства и представления массивов, создание их копий
import numpy as np


def main():
    # Метод view() для создания представления.
    # У каждого массива array существует метод view(), который возвращает
    # копию его представления. О чем здесь речь?
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    b = a
    print(id(a))
    print(a)
    print(id(b))
    print(b)
    a.shape = (3, 3)
    print(a)
    print(b)


if __name__ == '__main__':
    main()
