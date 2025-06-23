import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the constant sqrt(3)
sqrt3 = mp.sqrt(3)

# Compute natural logarithm of 3
ln3 = mp.log(3)

# Compute the inner expression: (3/2)*ln(3) - 1
inner_expr = (3/2)*ln3 - 1

# Compute the coefficient: pi / (6 * sqrt(3))
coeff = mp.pi / (6 * sqrt3)

# Multiply coefficient by inner expression to get final result
result = coeff * inner_expr

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))