import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply by pi to get final result
result = mp.pi * sqrt_2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))