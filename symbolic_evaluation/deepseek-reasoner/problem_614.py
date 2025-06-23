import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate the simple fraction 1/2 using high-precision arithmetic
numerator = mp.mpf(1)
denominator = mp.mpf(2)
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))