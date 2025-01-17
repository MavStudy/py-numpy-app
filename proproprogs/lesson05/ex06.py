# Изменение формы массивов, добавление и удаление осей
import numpy as np


def main():
    # Добавление и удаление осей
    #
    # Часто при работе с массивами NumPy требуется добавлять новые оси
    # измерений и удалять существующие. Есть множество способов выполнять эти
    # операции, но мы рассмотрим два наиболее распространенных с помощью
    # функций:
    # np.expand_dims(a, axis)  - добавление новой оси;
    # np.squeeze(a[, axis])  - удаление оси (без удаления элементов).

    # Давайте предположим, что у нас имеется некий многомерный массив:
    x_test = np.arange(32).reshape(8, 2, 2)  # массив 8х2х2
    print(
        "x_test - первоначальный массив",
        id(x_test),
        x_test.shape
    )
    print(x_test)

    print('-' * 70)

    # И нам потребовалось добавить еще одно измерение (ось), причем, в самое
    # начало, то есть, ось axis0. Сейчас на этой оси 8 элементов – матриц 2x2,
    # но мы хотим сделать четырехмерный массив, сохранив остальные три оси и их
    # данные без изменений. Как раз это достаточно просто сделать с помощью
    # функции expand_dims, следующим образом:

    x_test4 = np.expand_dims(x_test, axis=0)
    print(f"{x_test4.shape=}")  # (1, 8, 2, 2)
    print(
        "x_test4 - массив",
        id(x_test4),
        x_test4.shape
    )
    print(x_test4)

    print('-' * 70)

    # Видим, что массив стал четырехмерным и первая добавленная ось axis0
    # содержит один элемент – трехмерный массив 8x2x2. При необходимости, мы
    # всегда можем добавить новый элемент на эту ось:
    a = np.append(x_test4, x_test4, axis=0)

    print(
        "a - массив",
        id(a),
        a.shape
    )
    print(a)

    print('-' * 70)

    # или удалить ненужные элементы:
    b = np.delete(a, 0, axis=0)  # размерность (1, 8, 2, 2)
    # Здесь второй параметр 0 – индекс удаляемого элемента на оси axis0.
    print(
        "b - массив",
        id(b),
        b.shape
    )
    print(b)

    print('-' * 70)

    # Если нам нужно добавить последнюю ось в массиве, то для этого можно
    # записать такую команду:
    b = np.expand_dims(x_test4, axis=-1)  # размерность (1, 8, 2, 2, 1)

    # Отрицательный индекс -1 – это следующая с конца ось. Если указать
    # индекс -2, то добавится предпоследняя ось и так далее. Отрицательные
    # индексы очень удобно использовать при работе с массивами произвольных
    # размерностей.

    print(
        "b - массив",
        id(b),
        b.shape
    )
    print(b)

    print('-' * 70)

    # Следующая функция squeeze позволяет удалить все оси с одним элементом.
    # Например, строчка:
    c = np.squeeze(b)  # размерность (8, 2, 2)
    # превращает массив размерностью (1, 8, 2, 2)
    # в массив размерностью (8, 2, 2).

    print(
        "c - массив",
        id(c),
        c.shape
    )
    print(c)

    print('-' * 70)

    # При необходимости, дополнительно мы можем самостоятельно указать оси,
    # которые следует удалять, например, так:
    c = np.squeeze(b, axis=0)   # удалить только ось axis0, не затронув другие

    # Но, если указать ось с числом элементов больше 1, то возникнет ошибка:
    # c = np.squeeze(b, axis=1)  # ошибка, на оси axis1 8 элементов

    print(
        "c - массив",
        id(c),
        c.shape
    )
    print(c)

    print('-' * 70)


if __name__ == '__main__':
    main()
