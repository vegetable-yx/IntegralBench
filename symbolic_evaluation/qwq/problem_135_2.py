import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate 3 times pi
three_times_pi = 3 * mp.pi

# Divide by 4 to get the final result
result = three_times_pi / 4

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))