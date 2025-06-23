import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Extract the constant pi
pi_value = mp.pi

# Define the denominator
denominator = 12

# Compute the result: pi/12
result = pi_value / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))