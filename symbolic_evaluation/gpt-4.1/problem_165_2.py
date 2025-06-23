import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate the inner expression: 1 / sqrt(5)
sqrt_5 = mp.sqrt(5)  # Compute square root of 5
reciprocal_sqrt_5 = 1 / sqrt_5  # Compute reciprocal of sqrt(5)

# Compute the arccosine of the reciprocal
result = mp.acos(reciprocal_sqrt_5)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))