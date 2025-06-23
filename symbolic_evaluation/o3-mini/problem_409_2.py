import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Compute the first term: (5 * pi) / 24
term1 = (5 * mp.pi) / 24

# Compute the constant sqrt(3)
sqrt3 = mp.sqrt(3)

# Compute the argument for the logarithm: (sqrt(3) + 1) / (sqrt(3) - 1)
log_arg = (sqrt3 + 1) / (sqrt3 - 1)

# Compute the natural logarithm of the argument
log_val = mp.log(log_arg)

# Compute the coefficient: 1/(12 * sqrt(3))
coeff = 1 / (12 * sqrt3)

# Compute the second term: coefficient multiplied by the logarithm
term2 = coeff * log_val

# Sum both terms to get the final result
result = term1 + term2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))