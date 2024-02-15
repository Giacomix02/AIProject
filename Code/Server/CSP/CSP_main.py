from constraint import *


def run_csp(values: list, results_limit: int = None, upper_limit: int = None, lower_limit: int = None) -> list:
    porco = Problem()

    if results_limit is None:
        results_limit = 10
    if upper_limit is None:
        upper_limit = 100
    if lower_limit is None:
        lower_limit = 0

    for index in range(0, len(values)):
        porco.addVariable(variable=index, domain=[0, 1])
        temp = "X" + str(index)
        porco.addVariable(temp, [values[index]])

    porco.addVariable('results_limit', [results_limit])
    porco.addVariable('upper_limit', [upper_limit])
    porco.addVariable('lower_limit', [lower_limit])

    # print(porco.getSolutions())
    porco.addConstraint(lambda a, b, c, d, e, f, g, h, j, m, n:
                        a + b + c + d + e + f + g + h + j + m <= n,
                        (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'results_limit'))
    for index in range(0, len(values)):
        temp = "X" + str(index)
        porco.addConstraint(times_le, (index, temp, 'upper_limit'))
        porco.addConstraint(times_ge, (index, temp, 'lower_limit'))

    sol = porco.getSolutions()
    print(sol)
    return sol


def times_le(x, y, z):
    mul = x * y
    return mul <= z


def times_ge(x, y, z):
    mul = x * y
    return mul >= z
