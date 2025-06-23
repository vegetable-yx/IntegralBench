import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the denominator as an exact decimal value
denominator = mp.mpf('435.07')

# Compute the result: π divided by 435.07
result = mp.pi / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))