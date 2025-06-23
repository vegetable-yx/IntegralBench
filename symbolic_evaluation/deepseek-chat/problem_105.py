import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the constant π
pi_value = mp.pi

# Compute π/2
result = pi_value / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))