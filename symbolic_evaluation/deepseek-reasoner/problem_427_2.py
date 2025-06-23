import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate square roots
sqrt_11 = mp.sqrt(11)
sqrt_6 = mp.sqrt(6)

# Compute terms with coefficients
term1 = 21 * sqrt_11
term2 = 6 * sqrt_6

# Sum the terms and divide by 10
total = term1 + term2
result = total / 10

# Print result with 10 decimal places
print(mp.nstr(result, n=10))