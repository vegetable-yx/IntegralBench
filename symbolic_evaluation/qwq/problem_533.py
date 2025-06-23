import mpmath as mp

# Set precision to 15 decimal places
mp.dps = 15

# Define numerator and denominator as mpf values
numerator = mp.mpf(8)
denominator = mp.mpf(7)

# Compute the division
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))