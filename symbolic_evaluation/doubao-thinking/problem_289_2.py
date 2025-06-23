import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate the exact fraction 1/4 using arbitrary precision
result = mp.mpf(1)/4

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))