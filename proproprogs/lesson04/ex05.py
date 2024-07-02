# Свойства и представления массивов, создание их копий
import numpy as np


def main():
    # Метод view() для создания представления.
    # У каждого массива array существует метод view(), который возвращает
    # копию его представления. О чем здесь речь?
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    b = np.array(a)   # создaётся копия массива

    # Или же, копию можно получить с помощью метода copy объекта array:
    c = a.copy()  # создание копии массива

    # При этом происходит копирование всех свойств объекта array. Последний
    # вариант предпочтителен, когда нам нужно получить полную копию массива,
    # а не просто новый объект array.

    print(id(a), a.shape)
    print(a)
    print(id(b), b.shape)
    print(b)
    print(id(c), c.shape)
    print(c)

    print('-' * 30)

    b[0] = 10

    print(id(a), a.shape, a.dtype)
    print(a)
    print(id(b), b.shape, b.dtype)
    print(b)
    print(id(c), c.shape, c.dtype)
    print(c)


if __name__ == '__main__':
    main()
