import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define numerator and denominator as mpmath floating-point numbers
numerator = mp.mpf(1)
denominator = mp.mpf(4)

# Compute the fraction: 1/4
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))