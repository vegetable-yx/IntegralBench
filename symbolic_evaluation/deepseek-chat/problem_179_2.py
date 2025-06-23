import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the fraction: 1 divided by 8
numerator = mp.mpf(1)
denominator = mp.mpf(8)

# Compute the result of the fraction
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))