import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Directly use the mpmath constant for pi
result = mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))