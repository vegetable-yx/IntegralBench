import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π/4
pi_over_4 = mp.pi / 4

# Calculate 1/2
half = mp.mpf(1)/2

# Subtract to get the final result
result = pi_over_4 - half

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))