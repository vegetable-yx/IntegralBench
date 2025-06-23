import mpmath as mp
mp.dps = 15

# Calculate the integral result as 3 times pi
integral_value = 3 * mp.pi

# Set final result
result = integral_value

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))