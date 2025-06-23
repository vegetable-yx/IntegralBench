import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the analytical expression: 625 divided by 4
numerator = mp.mpf(625)
denominator = mp.mpf(4)
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))