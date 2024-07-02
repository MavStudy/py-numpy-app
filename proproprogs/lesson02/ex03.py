import numpy as np


def main():
    a = np.array([1, 2, 5000, 1000])
    print(a, a.dtype)

    # а можно привести к комплексному представлению
    b = np.complex64(a)
    print(b, b.dtype)
    # [1.e+00+0.j 2.e+00+0.j 5.e+03+0.j 1.e+03+0.j] complex64

    # И, обратно, из комплексного представления можем перейти в целочисленное:
    c = np.int32(b)
    print(c, c.dtype)
    # Вконсолиувидимпредупреждение, что мнимая информация о числе будет
    # утеряна, но массив будет успешно преобразован.



if __name__ == '__main__':
    main()