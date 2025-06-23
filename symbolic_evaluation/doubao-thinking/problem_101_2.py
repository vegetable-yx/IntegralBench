import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate arcsin(1/4) using mpmath's asin function
arcsin_val = mp.asin(mp.mpf(1)/4)

# Calculate the coefficient term -7/4
coefficient = -mp.mpf(7)/4

# Compute first part of the expression: -7/4 * arcsin(1/4)
term1 = coefficient * arcsin_val

# Calculate square root of 15 using mpmath's sqrt
sqrt_15 = mp.sqrt(15)

# Compute second part of the expression: sqrt(15)/8
term2 = sqrt_15 / 8

# Combine both terms for final result
result = term1 + term2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))