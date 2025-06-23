import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π and raise it to the third power
pi_cubed = mp.pi ** 3

# Multiply by 2 to get the final result
result = 2 * pi_cubed

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))