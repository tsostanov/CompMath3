import numpy as np


def variant_equation(x):
    return x ** 3 - 3 * x ** 2 + 7 * x - 10


def trigonometric_equation(x):
    return np.cos(x ** 2) + np.sin(x)


def interesting_equation(x):
    return np.exp(-x ** 2) * np.sin(x)


def print_variant_equation_description():
    print("1-ое уравнение:")
    print("f(x) = x^3 - 3x^2 + 7x - 10\n")


def print_trigonometric_equation_description():
    print("2-ое уравнение:")
    print("f(x) = cos(x^2) + sin(x)\n")


def print_interesting_equation_description():
    print("3-тье уравнение:")
    print("f(x) = exp(-x^2) * sin(x)\n")
