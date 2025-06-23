import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the fraction: 128 divided by 153
numerator = mp.mpf(128)
denominator = mp.mpf(153)
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))