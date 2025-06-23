import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by -3
product = -3 * sqrt2

# Multiply by pi to get final result
result = product * mp.pi

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))