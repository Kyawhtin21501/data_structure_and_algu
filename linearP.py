from pulp import LpProblem, LpVariable, LpMaximize, lpSum


model = LpProblem("Choose_Life_Partner", LpMaximize)


fun = {"A": 8, "B": 6, "C": 7}
comfort = {"A": 7, "B": 9, "C": 6}
future = {"A": 6, "B": 7, "C": 9}
time_required = {"A": 4, "B": 5, "C": 6}  


x = {person: LpVariable(f"x_{person}", cat="Binary") for person in ["A", "B", "C"]}

model += lpSum([fun[p] + comfort[p] + future[p] for p in x])

model += lpSum([time_required[p] * x[p] for p in x]) <= 10
model.solve()
for p in x:
    if x[p].value() == 1:
        print(f"Result: {p} さん")
