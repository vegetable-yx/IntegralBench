import mpmath as mp
mp.dps = 15  # Set internal precision

# Directly use mpmath's built-in constant for pi
result = mp.pi

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))