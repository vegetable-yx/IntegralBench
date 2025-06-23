import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate 2 * π
two_pi = 2 * mp.pi

# Compute square root of (2π)
sqrt_two_pi = mp.sqrt(two_pi)

# Apply the negative sign
result = -sqrt_two_pi

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))