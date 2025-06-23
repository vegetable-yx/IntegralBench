import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Assign the mathematical constant π to result
result = mp.pi

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))