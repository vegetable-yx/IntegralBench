import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Define the numerator
numerator = mp.mpf(4)

# Define the denominator as pi
denominator = mp.pi

# Compute the result: 4 divided by pi
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))