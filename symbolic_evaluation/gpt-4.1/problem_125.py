import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Compute the cube of pi
pi_cubed = mp.pi ** 3

# Divide by 128 to get the result
result = pi_cubed / 128

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))