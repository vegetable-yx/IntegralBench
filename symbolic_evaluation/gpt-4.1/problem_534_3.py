import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Multiply the square roots to get sqrt(2*pi)
sqrt_2pi = sqrt2 * sqrt_pi

# Multiply by 2 to get the final result
result = 2 * sqrt_2pi

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))