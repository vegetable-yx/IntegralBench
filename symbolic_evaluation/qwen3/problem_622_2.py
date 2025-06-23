import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator (π - 2)
numerator = mp.pi - 2

# Divide by 4 to get the final result
result = numerator / 4

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))