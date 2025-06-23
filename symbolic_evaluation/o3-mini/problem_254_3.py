import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant -3π
pi_value = mp.pi  # Get π from mpmath
result = -3 * pi_value  # Multiply by -3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))