import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Catalan's constant
G = mp.catalan

# Square Catalan's constant
G_squared = G**2

# Multiply by 2
result = 2 * G_squared

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))