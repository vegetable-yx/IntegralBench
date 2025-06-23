import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Compute (sqrt(2) - 1)
sqrt2_minus_1 = sqrt2 - 1

# Multiply by pi
result = mp.pi * sqrt2_minus_1

# Print result with 10 decimal places
print(mp.nstr(result, n=10))