import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate pi to the third power
pi_cubed = mp.pi ** 3

# Divide the result by 3
result = pi_cubed / 3

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))