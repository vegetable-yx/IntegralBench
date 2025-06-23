import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate denominator sqrt(2)
sqrt2 = mp.sqrt(2)

# Compute coefficient 4/sqrt(2)
coefficient = 4 / sqrt2

# Calculate hyperbolic sine of 1
sinh_1 = mp.sinh(1)

# Compute (sinh(1) - 1)
sinh_term = sinh_1 - 1

# Multiply components to get final result
result = coefficient * sin_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))