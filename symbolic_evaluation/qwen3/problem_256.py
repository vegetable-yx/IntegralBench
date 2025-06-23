import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by sqrt(2)
pi_sqrt2 = mp.pi * sqrt2

# Multiply by -3 to get final result
result = -3 * pi_sqrt2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))