import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Define the constant π (pi)
pi_value = mp.pi

# Define the denominator
denominator = 2

# Compute π divided by 2
result = pi_value / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))