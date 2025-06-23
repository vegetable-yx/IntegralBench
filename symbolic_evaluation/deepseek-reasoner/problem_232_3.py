import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi using mpmath's built-in constant
result = mp.pi

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))