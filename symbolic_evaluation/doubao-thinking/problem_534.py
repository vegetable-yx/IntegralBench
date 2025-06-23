import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Multiply by 2 to get final result
result = 2 * sqrt_pi

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))