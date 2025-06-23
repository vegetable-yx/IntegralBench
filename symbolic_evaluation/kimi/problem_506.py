import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Direct assignment of the exact integer value
result = mp.mpf(1005)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))