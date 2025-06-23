import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Define the numerator: 46,656
numerator = 46656

# Define the denominator: 5,785,642,924 multiplied by pi
denominator = 5785642924 * mp.pi

# Compute the result: numerator divided by denominator
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))