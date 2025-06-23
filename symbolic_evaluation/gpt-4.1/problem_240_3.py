import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate sqrt(2) to use in both numerator and denominator
sqrt2 = mp.sqrt(2)

# Compute numerator: 3 + 2*sqrt(2)
numerator = 3 + 2 * sqrt2

# Compute denominator: sqrt(2)
denominator = sqrt2

# Calculate the fraction: (3 + 2*sqrt(2)) / sqrt(2)
fraction = numerator / denominator

# Compute the natural logarithm of the fraction
result = mp.log(fraction)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))