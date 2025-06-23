import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the exact fraction 1/3 using arbitrary precision arithmetic
numerator = mp.mpf(1)
denominator = mp.mpf(3)
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))