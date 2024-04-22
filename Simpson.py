from tabulate import tabulate


def simpson_method(func, left, right, initial_n, accuracy):
    table = [["N", "n", "I", "runge"]]
    n = initial_n
    h = (right - left) / n
    iter_count = 1

    x_values = [left + i * h for i in range(n + 1)]
    y_values = [func(x) for x in x_values]

    integral = h / 3 * (y_values[0] + 4 * sum(y_values[1:n-1:2]) + 2 * sum(y_values[2:n-2:2]) + y_values[n])

    integral_prev = integral
    table.append([iter_count, n, integral, " "])

    while True:
        iter_count += 1
        n *= 2
        h /= 2

        x_values = [left + i * h for i in range(n + 1)]
        y_values = [func(x) for x in x_values]

        integral = h / 3 * (y_values[0] + 4 * sum(y_values[1:n-1:2]) + 2 * sum(y_values[2:n-2:2]) + y_values[n])

        runge = abs((integral - integral_prev) / (2 ** 4 - 1))
        table.append([iter_count, n, integral, runge])
        if runge < accuracy:
            break

        integral_prev = integral

    print("Метод Симпсона")
    print(tabulate(table, headers="firstrow", tablefmt="grid"))
    print("Значение интеграла: ", integral)
    print("Число разбиений:", n)

    return table
