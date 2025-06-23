import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate 1/128 using exact fractional arithmetic
numerator = mp.mpf(1)
denominator = mp.mpf(128)
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))