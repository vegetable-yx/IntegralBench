import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate the arctangent of 2
atan_val = mp.atan(2)

# Compute the expression inside the parentheses: (arctan(2) - 4)
inner_expr = atan_val - 4

# Multiply by π/4
pi_over_4 = mp.pi / 4
result = pi_over_4 * inner_expr

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))