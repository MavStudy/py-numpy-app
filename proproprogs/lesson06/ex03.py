# NumPy - Объединение и разделение массивов
import numpy as np


def main():
    # Аналогичным образом происходит объединение и одномерных массивов:
    a = np.fromstring('1 2 3 4', sep=' ')
    b = np.fromstring('5 6 7 8', sep=' ')

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
    c = np.hstack([a, b])  # объединение по оси axis1
    d = np.vstack([a, b])  # объединение по оси axis0 (размерность 6х3x2)

    print(
        f"массив c",
        id(c),
        c.shape
    )
    print(c)
    # массив c 42865648(8, )
    # [1. 2. 3. 4. 5. 6. 7. 8.]

    print(
        f"массив d",
        id(d),
        d.shape
    )
    print(d)
    # массив d 161766544 (2, 4)
    # [[1. 2. 3. 4.]
    #  [5. 6. 7. 8.]]

    print('-' * 70)


if __name__ == '__main__':
    main()
