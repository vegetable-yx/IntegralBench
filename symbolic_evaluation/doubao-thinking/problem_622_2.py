import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π/4
term1 = mp.pi / 4

# Calculate 1/2
term2 = mp.mpf(1)/2

# Compute the final result: π/4 - 1/2
result = term1 - term2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))