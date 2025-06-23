import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate pi cubed
pi_cubed = mp.pi ** 3

# Divide by 32 to get the final result
result = pi_cubed / 32

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))