import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Define the numerator and denominator
numerator = mp.mpf(1)
denominator = mp.mpf(3)

# Compute the result: 1/3
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))