import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π/4
pi_over_4 = mp.pi / 4

# Compute 1/2
half = mp.mpf(1)/2

# Subtract: π/4 - 1/2
result = pi_over_4 - half

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))