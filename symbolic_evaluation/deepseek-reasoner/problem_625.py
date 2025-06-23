import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by pi
pi_times_sqrt2 = mp.pi * sqrt2

# Divide by 4 to get the final result
result = pi_times_sqrt2 / 4

print(mp.nstr(result, n=10))