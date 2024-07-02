# NumPy - базовые математические операции над массивами
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
    # Пусть у нас задан тот же одномерный массив:
    a = np.array([1, 2, 3])
    array_info('a', a)
    print(a)
    # массив a: <class 'numpy.ndarray'> 30912848 (3,)
    # [1 2 3]

    separator()

    # Все указанные в таблице операции выполняются следующим образом:
    a1 = -a  # унарный минус
    array_info('a1', a1)
    print(a1)
    # массив a1: <class 'numpy.ndarray'> 41835568 (3,)
    # [-1 -2 -3]

    separator()

    a2 = a + 2  # сложение с числом
    # так тоже можно записывать
    # a2 = 2 + a
    array_info('a2', a2)
    print(a2)
    # массив a2: <class 'numpy.ndarray'> 161770160 (3,)
    # [3 4 5]

    separator()

    a3 = a - 3  # вычитание числа
    array_info('a3', a3)
    print(a3)
    # массив a3: <class 'numpy.ndarray'> 161766064 (3,)
    # [-2 -1  0]

    separator()

    a4 = a * 5  # умножение на число
    array_info('a4', a4)
    print(a4)
    # массив a4: <class 'numpy.ndarray'> 161762064 (3,)
    # [ 5 10 15]

    separator()

    a5 = a / 5  # деление на число
    array_info('a5', a5)
    print(a5)
    # массив a5: <class 'numpy.ndarray'> 161765968 (3,)
    # [0.2 0.4 0.6]

    separator()

    a6 = a // 5  # челочисленное деление
    array_info('a6', a6)
    print(a6)
    # массив a6: <class 'numpy.ndarray'> 161766448 (3,)
    # [0 0 0]

    separator()

    a7 = a ** 3  # возведение в степень 3
    array_info('a7', a7)
    print(a7)
    # массив a7: <class 'numpy.ndarray'> 161762352 (3,)
    # [ 1  8 27]

    separator()

    a8 = a % 2  # вычисление по мудулю 2
    array_info('a8', a8)
    print(a8)
    # массив a8: <class 'numpy.ndarray'> 161762544 (3,)
    # [1 0 1]

    separator()

    # Разумеется, приоритеты этих операций такие же, что и при обычных
    # математических вычислениях. А на выходе мы получаем новый массив
    # с соответствующими значениями.


if __name__ == '__main__':
    main()
