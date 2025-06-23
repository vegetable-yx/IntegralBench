import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute sqrt(2)
sqrt2 = mp.sqrt(2)

# Compute the argument inside the logarithm: 3 + 2*sqrt(2)
log_arg = 3 + 2 * sqrt2

# Compute the natural logarithm of the argument
log_val = mp.log(log_arg)

# Compute the coefficient: 7 / (4 * sqrt(2))
coeff = 7 / (4 * sqrt2)

# Multiply coefficient by logarithm
term2 = coeff * log_val

# First term: -1/2
term1 = -0.5

# Sum the two terms
result = term1 + term2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))