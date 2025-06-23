import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Assign the constant π to a variable
result = mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))