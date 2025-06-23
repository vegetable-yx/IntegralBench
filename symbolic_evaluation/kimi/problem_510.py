import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Compute denominator: 3 * sqrt(3)
denominator = 3 * sqrt3

# Calculate final result: pi divided by denominator
result = mp.pi / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))