import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# The analytical result is a simple integer value
result = mp.mpf(336)

# Print the result with 10 decimal place formatting
print(mp.nstr(result, n=10))