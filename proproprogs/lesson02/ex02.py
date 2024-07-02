import numpy as np


def main():
    a = np.array([1, 2, 5000, 1000], dtype='int8')
    print(a, a.dtype)
    # Error:
    #
    # [   1    2 -120  -24] int8
    #
    # Почему так? Потому что значения 5000 и 1000 не умещаются в
    # однобайтовое целое число, поэтому видим значения -120 и -24. 


if __name__ == '__main__':
    main()
