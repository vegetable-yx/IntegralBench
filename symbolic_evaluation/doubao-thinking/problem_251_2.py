import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Compute (sqrt(2) - 1)
sqrt_minus_1 = sqrt2 - 1

# Multiply by 4π
result = 4 * mp.pi * sqrt_minus_1

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))