import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by pi
pi_times_sqrt2 = mp.pi * sqrt2

# Divide by 4 to get final result
result = pi_times_sqrt2 / 4

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))