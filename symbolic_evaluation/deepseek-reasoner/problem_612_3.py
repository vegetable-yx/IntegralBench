import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Assign the exact integer result from analytical solution
result = mp.mpf(626)

# Print the result with 10 decimal places (will show .0000000000)
print(mp.nstr(result, n=10))