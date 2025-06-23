import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define numerator and denominator as exact mpmath floating-point numbers
numerator = mp.mpf(2023)
denominator = mp.mpf(2022)

# Compute the exact fraction
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))