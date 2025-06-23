import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Assign the constant π to result
result = mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))