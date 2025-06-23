import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi raised to the power of 3
pi_cubed = mp.pi ** 3

# Divide the result by 16 to get the final value
result = pi_cubed / 16

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))