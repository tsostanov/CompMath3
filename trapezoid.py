from tabulate import tabulate


def trapezoidal_method(func, left, right, initial_n, accuracy):
    table = [["N", "n", "I", "runge"]]
    n = initial_n
    h = (right - left) / n
    iter_count = 1

    integral = (func(left) + func(right)) / 2
    for i in range(1, n):
        x = left + i * h
        integral += func(x)

    integral *= h

    integral_prev = integral
    table.append([iter_count, n, integral, " "])

    while True:
        iter_count += 1
        n *= 2
        h /= 2
        integral = (func(left) + func(right)) / 2

        for i in range(1, n):
            x = left + i * h
            integral += func(x)

        integral *= h

        runge = abs((integral - integral_prev) / (2 ** 2 - 1))
        table.append([iter_count, n, integral, runge])
        if runge < accuracy:
            break

        integral_prev = integral

    print("Метод трапеций")
    print(tabulate(table, headers="firstrow", tablefmt="grid"))
    print("Значение интеграла: ", integral)
    print("Число разбиений:", n)

    return table
