import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi to the third power
pi_cubed = mp.pi ** 3

# Calculate first term: π³/48
term1 = pi_cubed / 48

# Calculate second term: π/4
term2 = mp.pi / 4

# Final result: term1 - term2
result = term1 - term2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))