import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Assign the constant π to the result variable
result = mp.pi

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))