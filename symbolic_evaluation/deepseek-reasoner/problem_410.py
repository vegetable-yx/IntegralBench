import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate the constant e
e = mp.e

# Compute denominator 2e
denominator = 2 * e

# Calculate the final result
result = sqrt_pi / denominator

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))