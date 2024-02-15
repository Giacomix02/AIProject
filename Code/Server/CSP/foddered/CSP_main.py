from constraintGraph import Variable, Constraint, renderGraph
from dfs import dfs_solve_all


def run_csp(values: list, results_limit: int = None, upper_limit: int = None, lower_limit: int = None) -> list:
    domain = [0, 1]
    variables = [Variable("X0", domain),
                 Variable("X1", domain),
                 Variable("X2", domain),
                 Variable("X3", domain),
                 Variable("X4", domain),
                 Variable("X5", domain),
                 Variable("X6", domain),
                 Variable("X7", domain),
                 Variable("X8", domain),
                 Variable("X9", domain)]
    if results_limit is None:
        results_limit = 10
    if upper_limit is None:
        upper_limit = 100
    if lower_limit is None:
        lower_limit = 0

    constraint = []

    constraint.append(Constraint([var for var in variables],
                                 lambda a, b, c, d, e, f, g, h, j, m:
                                 a + b + c + d + e + f + g + h + j + m == results_limit,
                                 f"sum(X0, ... ,X9) <= {results_limit}"
                                 )
                      )
    for i in range(0, 9):
        constraint.append(Constraint([variables[i]],
                                     lambda x:
                                     (x * values[i]) <= upper_limit,
                                     f"X{i}*{values[i]} <= {upper_limit}"))
        constraint.append(Constraint([variables[i]],
                                     lambda x:
                                     (x * values[i]) >= lower_limit,
                                     f"X{i}*{values[i]} >= {lower_limit}"))
    csp = renderGraph(variables, constraint)
    print(csp.constraints)
    return dfs_solve_all(csp)
