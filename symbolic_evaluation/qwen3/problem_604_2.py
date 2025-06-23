import mpmath as mp
mp.dps = 15  # Set internal precision

# The analytical solution is simply to 1
result = mp.mpf(1)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))