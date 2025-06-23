import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by pi to get final result
pi_times_sqrt2 = mp.pi * sqrt2

# Print result with 10 decimal places
print(mp.nstr(pi_times_sqrt2, n=10))