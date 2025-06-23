import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of 5
sqrt5 = mp.sqrt(5)

# Compute (sqrt(5) - 1)
sqrt5_minus_1 = sqrt5 - 1

# Multiply by pi/2
result = (mp.pi / 2) * sqrt5_minus_1

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))