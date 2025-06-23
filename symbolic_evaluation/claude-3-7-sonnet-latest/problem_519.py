import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant π/4
pi_value = mp.pi  # Get the value of π
result = pi_value / 4  # Divide π by 4

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))