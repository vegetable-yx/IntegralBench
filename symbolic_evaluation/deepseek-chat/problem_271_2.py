import mpmath as mp

# Set the internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate the numerator: pi (mpmath constant) minus 3
numerator = mp.pi - 3

# Denominator is 128
denominator = 128

# Compute the result by dividing the numerator by the denominator
result = numerator / denominator

# Print the result to exactly 10 decimal places using mp.nstr
print(mp.nstr(result, n=10))