import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute pi cubed
pi_cubed = mp.pi ** 3

# Divide by 4 to get the result
result = pi_cubed / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))