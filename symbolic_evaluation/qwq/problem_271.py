import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the numerator (19 * π)
numerator = mp.mpf(19) * mp.pi

# Divide by 512 to get the final result
result = numerator / mp.mpf(512)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))