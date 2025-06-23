import mpmath as mp

# Set the internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate π and raise it to the 3/2 power
pi_term = mp.pi ** (3/2)

# Calculate the square root of 2
sqrt_two = mp.sqrt(2)

# Compute the final result by dividing π^(3/2) by sqrt(2)
result = pi_term / sqrt_two

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))