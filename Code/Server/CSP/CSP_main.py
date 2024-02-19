from Code.Server.CSP.constraintGraph import Variable, Constraint, renderGraph
from Code.Server.CSP.dfs import dfs_solve1


def run_csp(values: list, upper_limit: int = None, lower_limit: int = None):
    if values is None:
        return None

    domain = [1, 0]  # dominio delle variabili 0-1
    variables = []
    for i in range(0, 10):  # aggiungo in alternanza le variabili X 0-1 e le variabili V valore della previsione
        variables.append(Variable("X" + str(i), domain=domain))
        variables.append(Variable('V' + str(i), [values[i]]))

    if upper_limit is None:
        upper_limit = 101
    if lower_limit is None:
        lower_limit = -1
    constraint = []

    j = 0
    for i in range(0, 20,
                   2):  # procedo 2 per volta, quindi ogni loop avrò da aggiungere ai constraint Xn (i) e Vn (i+1)
        constraint.append(Constraint([variables[i], variables[i + 1]], # contraints per filtrare i valori in un intervallo
                                     lambda x, y:
                                     (lower_limit <= y <= upper_limit and x == 1) # se il valore rientra nell'intervallo e la variabile è 1 accettare
                                     or # oppure
                                     (not (lower_limit <= y <= upper_limit) and x == 0), # se il valore non rientra nell'intervallo e x è 0 accettare
                                     f"{lower_limit} <= X{j}*{values[j]} <= {upper_limit}"))
        j += 1
    csp = renderGraph(variables, constraint)
    results: dict = dfs_solve1(csp)

    return csp.variables, results

