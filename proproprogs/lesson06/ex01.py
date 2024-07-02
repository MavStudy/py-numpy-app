# NumPy - Объединение и разделение массивов
import numpy as np


def main():
    # Предположим у нас есть два двухмерных массива:
    a = np.array([(1, 2), (3, 4)])
    b = np.array([(5, 6), (7, 8)])

    print(
        f"массив a",
        id(a),
        a.shape
    )
    print(a)

    print(
        f"массив b",
        id(b),
        b.shape
    )
    print(b)

    print('-' * 70)

    # Их можно объединить как по горизонтали, так и по вертикали,
    # с помощью функций:
    c = np.hstack([a, b])  # объединение по оси axis1 (размерность 2х4)
    d = np.vstack([a, b])  # объединение по оси axis0 (размерность 4х2)

    print(
        f"массив c",
        id(c),
        c.shape
    )
    print(c)

    print(
        f"массив d",
        id(d),
        d.shape
    )
    print(d)

    print('-' * 70)


if __name__ == '__main__':
    main()
