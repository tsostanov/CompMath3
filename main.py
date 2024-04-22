import numpy as np
import matplotlib.pyplot as plt
from equations import variant_equation, trigonometric_equation, interesting_equation, \
    print_variant_equation_description, print_trigonometric_equation_description, print_interesting_equation_description
from squares import rectangle_method
from trapezoid import trapezoidal_method
from Simpson import simpson_method


def plot_equations(equation_system, left, right):
    x = np.linspace(left - 1, right + 1, 400)
    y = equation_system(x)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('График функции')
    plt.grid(True)
    plt.show()


def choose_equation():
    while True:
        print("Выберите уравнение:")
        print_variant_equation_description()
        print_trigonometric_equation_description()
        print_interesting_equation_description()
        choice = input("Введите номер уравнения (1, 2 или 3): ")

        if choice == '1':
            return variant_equation
        elif choice == '2':
            return trigonometric_equation
        elif choice == '3':
            return interesting_equation
        else:
            print("Некорректный выбор. Пожалуйста, введите номер системы заново.")


def main():
    equation = choose_equation()
    if equation:
        print("Выбранное уравнение:", equation.__name__)
        print("Введите пределы интегрирования")
        while True:
            try:
                left = float(input("Введите левый предел интегрирования: "))
                right = float(input("Введите правый предел интегрирования: "))

                if not (np.isfinite(left) and np.isfinite(right)):
                    raise ValueError("Введены некорректные значения. Пожалуйста, введите числа.")

                if left >= right:
                    raise ValueError("Левый предел интегрирования должен быть меньше правого.")

                print("Левый предел интегрирования:", left)
                print("Правый предел интегрирования:", right)

                plot_equations(equation, left, right)

                break
            except ValueError as e:
                print(e)
        accuracy = None
        while accuracy is None:
            try:
                accuracy = float(input("Введите точность вычисления: "))
                if accuracy <= 0:
                    raise ValueError("Точность должна быть положительным числом.")
            except ValueError as e:
                print(e)

        while True:
            print("Выберите метод численного интегрирования:")
            print("1. Метод прямоугольников")
            print("2. Метод трапеций")
            print("3. Метод Симпсона")

            method_choice = input("Введите номер метода (1, 2 или 3): ")

            if method_choice == '1':
                rectangle_method(equation, left, right, 4, accuracy)
                break
            elif method_choice == '2':
                trapezoidal_method(equation, left, right, 4, accuracy)
                break
            elif method_choice == '3':
                simpson_method(equation, left, right, 4, accuracy)
                break
            else:
                print("Некорректный выбор метода. Пожалуйста, введите номер метода от 1 до 3.")


if __name__ == "__main__":
    main()
