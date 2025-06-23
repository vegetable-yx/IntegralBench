import mpmath as mp

# Set internal decimal precision to 15 for accurate computations
mp.dps = 15

# Compute pi^3
pi_cubed = mp.pi ** 3

# Divide by 48 to get the result
result = pi_cubed / 48

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))