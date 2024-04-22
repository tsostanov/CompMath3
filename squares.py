from tabulate import tabulate


def rectangle_method(func, left, right, initial_n, accuracy):
    print("Метод средних прямоугольников:")
    midpoint_rectangle_method(func, left, right, initial_n, accuracy)
    print("\nМетод левых прямоугольников:")
    left_rectangle_method(func, left, right, initial_n, accuracy)
    print("\nМетод правых прямоугольников:")
    right_rectangle_method(func, left, right, initial_n, accuracy)


def midpoint_rectangle_method(func, left, right, initial_n, accuracy):
    table = [["N", "n", "I", "runge"]]
    n = initial_n
    h = (right - left) / n
    iter_count = 1

    integral = 0
    for i in range(n):
        x_left = left + i * h
        x_right = left + (i + 1) * h
        integral += func((x_right + x_left) / 2) * h

    integral_prev = integral
    table.append([iter_count, n, integral, " "])

    while True:
        iter_count += 1
        n *= 2
        h /= 2
        integral = 0
        for i in range(n):
            x_left = left + i * h
            x_right = left + (i + 1) * h
            integral += func((x_right + x_left) / 2) * h

        runge = abs((integral - integral_prev) / (2 ** 2 - 1))
        table.append([iter_count, n, integral, runge])
        if runge < accuracy:
            break

        integral_prev = integral

    print(tabulate(table, headers="firstrow", tablefmt="grid"))
    print("Значение интеграла: ", integral)
    print("Число разбиений:", n)


def left_rectangle_method(func, left, right, initial_n, accuracy):
    table = [["N", "n", "I", "runge"]]
    n = initial_n
    h = (right - left) / n
    iter_count = 1

    integral = 0
    for i in range(n):
        x_left = left + i * h
        x_right = left + (i + 1) * h
        integral += func(x_left) * h

    integral_prev = integral
    table.append([iter_count, n, integral, " "])

    while True:
        iter_count += 1
        n *= 2
        h /= 2
        integral = 0
        for i in range(n):
            x_left = left + i * h
            x_right = left + (i + 1) * h
            integral += func(x_left) * h

        runge = abs((integral - integral_prev) / (2 ** 2 - 1))
        table.append([iter_count, n, integral, runge])
        if runge < accuracy:
            break

        integral_prev = integral

    print(tabulate(table, headers="firstrow", tablefmt="grid"))
    print("Значение интеграла: ", integral)
    print("Число разбиений:", n)


def right_rectangle_method(func, left, right, initial_n, accuracy):
    table = [["N", "n", "I", "runge"]]
    n = initial_n
    h = (right - left) / n
    iter_count = 1

    integral = 0
    for i in range(n):
        x_left = left + i * h
        x_right = left + (i + 1) * h
        integral += func(x_right) * h

    integral_prev = integral
    table.append([iter_count, n, integral, " "])

    while True:
        iter_count += 1
        n *= 2
        h /= 2
        integral = 0
        for i in range(n):
            x_left = left + i * h
            x_right = left + (i + 1) * h
            integral += func(x_right) * h

        runge = abs((integral - integral_prev) / (2 ** 2 - 1))
        table.append([iter_count, n, integral, runge])
        if runge < accuracy:
            break

        integral_prev = integral

    print(tabulate(table, headers="firstrow", tablefmt="grid"))
    print("Значение интеграла: ", integral)
    print("Число разбиений:", n)
