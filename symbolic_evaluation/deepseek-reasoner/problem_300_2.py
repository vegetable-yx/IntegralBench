import mpmath as mp
mp.dps = 15  # Set internal precision

# The analytical solution is exactly 0
result = mp.mpf(0)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))