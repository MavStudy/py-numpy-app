# NumPy - Произведение матриц и векторов, элементы линейной алгебры
import numpy as np


def separator(sep='-'):
    print(sep * 70)


def array_info(name, arr):
    print(
        f"массив {name}:",
        type(arr),
        id(arr),
        arr.shape
    )


def main():
    # Векторное умножение
    #
    # Векторное_умножение.png
    #

    # Первое умножение реализуется через функцию:
    a = np.arange(1, 10)
    array_info('a', a)
    print(a)

    separator()

    b = np.ones(9)
    array_info('b', b)
    print(b)
    # np.dot(a, b)  # значение 45

    separator()

    print(f"{np.dot(a, b) = }")
    # np.dot(a, b) = 45.0

    separator()

    # Либо, более предпочтительной функцией для внутреннего умножения векторов:
    print(f"{np.inner(a, b) = }")
    # np.inner(a, b) = 45.0

    separator()

    # Второй вариант умножения (внешнее умножение векторов) реализуется
    # с помощью функции
    res2 = np.outer(a, b)
    array_info('res2', res2)
    print(res2)
    # массив res2: <class 'numpy.ndarray'> 2211027099376 (9, 9)
    # [[1. 1. 1. 1. 1. 1. 1. 1. 1.]
    #  [2. 2. 2. 2. 2. 2. 2. 2. 2.]
    #  [3. 3. 3. 3. 3. 3. 3. 3. 3.]
    #  [4. 4. 4. 4. 4. 4. 4. 4. 4.]
    #  [5. 5. 5. 5. 5. 5. 5. 5. 5.]
    #  [6. 6. 6. 6. 6. 6. 6. 6. 6.]
    #  [7. 7. 7. 7. 7. 7. 7. 7. 7.]
    #  [8. 8. 8. 8. 8. 8. 8. 8. 8.]
    #  [9. 9. 9. 9. 9. 9. 9. 9. 9.]]

    separator()

    # Операция умножения матриц и векторов используется довольно часто, поэтому
    # в пакете NumPy имеется весьма полезный перегруженный оператор, заменяющий
    # функцию matmul:
    print(f"{a @ b = }")
    # a @ b = 45.0

    separator()

    # или, с использованием матриц:
    a.resize(3, 3)
    array_info('a', a)
    print(a)
    # массив a: <class 'numpy.ndarray'> 2027089092144 (3, 3)
    # [[1 2 3]
    #  [4 5 6]
    #  [7 8 9]]

    separator()

    b.resize(3, 3)
    array_info('b', b)
    print(b)
    # массив b: <class 'numpy.ndarray'> 2027210219056 (3, 3)
    # [[1. 1. 1.]
    #  [1. 1. 1.]
    #  [1. 1. 1.]]

    separator()

    print(f"{a @ b = }")  # a @ b  -  аналог np.matmul(a, b)
    # a @ b = array([[ 6.,  6.,  6.],
    #                [15., 15., 15.],
    #                [24., 24., 24.]])


if __name__ == '__main__':
    main()
