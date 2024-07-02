# NumPy - Объединение и разделение массивов
import numpy as np


def main():
    # Для объединения массивов вдоль строго определенной оси можно
    # воспользоваться функцией concatenate(). Например, возьмем два трехмерных
    # массива:
    a = np.arange(1, 13)
    b = np.arange(13, 27)

    print(
        "массив a",
        id(a),
        a.shape
    )
    print(a)

    print(
        "массив b",
        id(b),
        b.shape
    )
    print(b)

    print('-' * 70)

    a.resize(3, 3, 2)
    b.resize(3, 3, 2)
    print(
        "массив a",
        id(a),
        a.shape
    )
    print(a)
    print()
    print(
        "массив b",
        id(b),
        b.shape
    )
    print(b)

    print('-' * 70)

    # И объединим их по каждой из осей:
    c0 = np.concatenate([a, b], axis=0)  # размерность 6х3х2
    c1 = np.concatenate([a, b], axis=1)  # размерность 3х6х2
    c2 = np.concatenate([a, b], axis=2)  # размерность 3х3х4

    print(
        "массив c0",
        id(c0),
        c0.shape
    )
    print(c0)

    print('-' * 70)

    print(
        "массив c1",
        id(c1),
        c1.shape
    )
    print(c1)

    print('-' * 70)

    print(
        "массив c2",
        id(c2),
        c2.shape
    )
    print(c2)

    print('-' * 70)


if __name__ == '__main__':
    main()
