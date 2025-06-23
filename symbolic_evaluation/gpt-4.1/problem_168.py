import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Retrieve mathematical constants
pi_val = mp.pi  # π constant
catalan_val = mp.catalan  # Catalan's constant G

# Compute the product π * G
result = pi_val * catalan_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))