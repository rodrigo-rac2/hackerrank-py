import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = numpy.array([[]], int)
    b = numpy.array([[]], int)
    for i in range(n):
        a = numpy.append(a, numpy.array([input().split()], int), axis=i-1)

    for i in range(n):
        b = numpy.append(b, numpy.array([input().split()], int), axis=i-1)

    # print(a + b)  # [  6.   8.  10.  12.]
    print(numpy.add(a, b))  # [  6.   8.  10.  12.]

    # print(a - b)  # [-4. -4. -4. -4.]
    print(numpy.subtract(a, b))  # [-4. -4. -4. -4.]

    # print(a * b)  # [  5.  12.  21.  32.]
    print(numpy.multiply(a, b))  # [  5.  12.  21.  32.]

    # print(a / b)  # [ 0.2         0.33333333  0.42857143  0.5       ]
    print(numpy.floor_divide(a, b))  # [ 0.2         0.33333333  0.42857143  0.5       ]

    # print(a % b)  # [ 1.  2.  3.  4.]
    print(numpy.mod(a, b))  # [ 1.  2.  3.  4.]

    # print(a ** b)  # [  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
    print(numpy.power(a, b))  # [  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
