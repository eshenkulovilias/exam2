def func(*args):
    summ = 0
    for i in args:
        try:
            summ += i
        except TypeError:
            continue
    return summ