import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the analytical expression: 4 divided by 5
numerator = mp.mpf(4)
denominator = mp.mpf(5)
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))