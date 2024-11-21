from sympy import symbols, Eq, solve

x = symbols('x')
equation = Eq(x**2 - 4, 0)
solutions = solve(equation, x)
print(solutions)
