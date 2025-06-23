import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi cubed
pi_cubed = mp.pi ** 3

# Divide by 288 to get the final result
result = pi_cubed / 288

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))