import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the square root of 2
sqrt2 = mp.sqrt(2)

# Compute pi
pi_val = mp.pi

# Divide the square root of 2 by pi
result = sqrt2 / pi_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))