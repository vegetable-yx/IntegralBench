import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define numerator and denominator
numerator = 3
denominator = 10

# Compute the fraction: 3/10
result = mp.mpf(numerator) / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))