import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define numerator and denominator as mpmath floating-point numbers
numerator = mp.mpf(2)
denominator = mp.mpf(5)

# Perform the division
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))