import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute pi using mpmath's constant
pi = mp.pi

# Calculate pi cubed
pi_cubed = pi ** 3

# Compute square root of 3
sqrt3 = mp.sqrt(3)

# Calculate the denominator (8 * sqrt(3))
denominator = 8 * sqrt3

# Compute the final result
result = pi_cubed / denominator

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))