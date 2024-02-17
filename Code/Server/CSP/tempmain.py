import CSP_main

csp = CSP_main.run_csp(values=[20, 30, 40, 50, 60, 70, 90, 80, 95, 5], lower_limit=80)
dict = csp[0]

print("#########################################")

array = []

for key in dict:
    if "X" in str(key):
        array.append(dict[key])

print(array)