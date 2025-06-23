import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Compute sinh(1)
sinh_val = mp.sinh(1)

# Compute cosh(1)
cosh_val = mp.cosh(1)

# Compute the expression inside the parentheses: 1 + sinh(1) - cosh(1)
inner_expr = 1 + sinh_val - cosh_val

# Multiply the result by 2
result = 2 * inner_expr

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))