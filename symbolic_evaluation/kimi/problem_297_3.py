import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the numerical value of 5π
five_pi = 5 * mp.pi

# Compute the numerator (16 - 5π)
numerator = 16 - five_pi

# Divide by 15 to get the final result
result = numerator / 15

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))