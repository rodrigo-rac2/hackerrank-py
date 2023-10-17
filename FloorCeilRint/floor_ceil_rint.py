import numpy as np
np.set_printoptions(legacy='1.13')


if __name__ == '__main__':
    a = np.array(input().split(), float)
    print(np.floor(a))
    print(np.ceil(a))
    print(np.rint(a))
