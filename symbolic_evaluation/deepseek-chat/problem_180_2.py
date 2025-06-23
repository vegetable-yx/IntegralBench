import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant π
pi_val = mp.pi

# Compute π/2
result = pi_val / 2

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))