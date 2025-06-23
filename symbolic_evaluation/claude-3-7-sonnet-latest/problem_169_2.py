import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate pi cubed
pi_cubed = mp.pi ** 3

# Divide by 8 to get the final result
result = pi_cubed / 8

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))