import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator: pi cubed
pi_val = mp.pi
pi_cubed = pi_val**3

# Define the denominator
denominator = 576

# Compute the result: pi^3 divided by 576
result = pi_cubed / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))