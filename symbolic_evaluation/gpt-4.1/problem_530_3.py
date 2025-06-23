import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate sqrt(2) once for reuse
sqrt2 = mp.sqrt(2)

# Compute the argument for the logarithm in term2: (sqrt(2) + 1) / (sqrt(2) - 1)
numerator = sqrt2 + 1
denominator = sqrt2 - 1
log_arg = numerator / denominator

# Term1: constant 3
term1 = 3

# Term2: (1/sqrt(2)) * ln(log_arg)
term2 = (1 / sqrt2) * mp.log(log_arg)

# Term3: sqrt(2) * ln(1 + sqrt(2))
term3 = sqrt2 * mp.log(1 + sqrt2)

# Combine the terms: result = term1 - term2 - term3
result = term1 - term2 - term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))