import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate pi cubed: π raised to the power of 3
pi_cubed = mp.pi ** 3

# Divide the result by 64 to obtain the final value
result = pi_cubed / 64

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))