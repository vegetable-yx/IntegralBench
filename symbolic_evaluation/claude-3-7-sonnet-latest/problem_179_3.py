import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the exact fraction 1/4 using high-precision arithmetic
numerator = mp.mpf(1)
denominator = mp.mpf(4)
result = numerator / denominator

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))