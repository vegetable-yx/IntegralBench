import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the square root of 5
sqrt5 = mp.sqrt(5)

# Compute the argument for the logarithm: (2 + sqrt(5))
log_arg = 2 + sqrt5

# Compute the natural logarithm of the argument: ln(2 + sqrt(5))
log_term = mp.log(log_arg)

# Compute the first term: pi * ln(2 + sqrt(5))
term1 = mp.pi * log_term

# Compute the coefficient for the second term: (sqrt(5) - 1)
coeff = sqrt5 - 1

# Compute the second term: (pi/2) * (sqrt(5) - 1)
term2 = (mp.pi / 2) * coeff

# Combine the terms: term1 - term2
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))