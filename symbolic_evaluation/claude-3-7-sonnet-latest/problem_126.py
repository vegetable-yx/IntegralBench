import mpmath as mp

# Set the internal decimal precision to 15 digits for calculations
mp.dps = 15

# Compute pi squared
pi_squared = mp.pi ** 2

# Compute the square root of 3
sqrt_3 = mp.sqrt(3)

# Calculate the denominator: 4 * sqrt(3)
denominator = 4 * sqrt_3

# Divide pi squared by the denominator to get the result
result = pi_squared / denominator

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))