import numpy as np


def getList():
    for i in range(10):
        yield i


def main():
    a = np.array((1, 2, 3, 4))
    print(a, type(a), a.dtype)
    # [1 2 3 4] <class 'numpy.ndarray'> int32

    b = np.array([x for x in getList()])
    print(b, type(b), b.dtype)
    # [0 1 2 3 4 5 6 7 8 9] <class 'numpy.ndarray'> int32

    c = np.array(range(5))
    print(c, type(c), c.dtype)
    # [0 1 2 3 4] <class 'numpy.ndarray'> int32

    d = np.array("Hello")
    print(d, type(d), d.dtype)
    # Hello <class 'numpy.ndarray'> <U5


if __name__ == '__main__':
    main()
