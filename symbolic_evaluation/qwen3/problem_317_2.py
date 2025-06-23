import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the fraction sqrt(2)/2
half_sqrt2 = sqrt2 / 2

# Calculate pi squared
pi_squared = mp.pi ** 2

# Multiply the two components and apply the negative sign
result = -half_sqrt2 * pi_squared

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))