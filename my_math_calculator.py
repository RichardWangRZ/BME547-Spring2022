def sqrt(n):
    if type(n) is str:
        raise TypeError("Cannnot send a string.")
    if n < 0:
        raise ValueError("{} is a negative number, not allowed."format(n))

    x = n
    y = 1
    e = 0.000001
    while(x - y > e):
        x = (x + y) / 2
        y = n / x
    return x
