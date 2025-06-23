import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate the exact fraction 1/2 using arbitrary precision
result = mp.mpf(1)/2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))