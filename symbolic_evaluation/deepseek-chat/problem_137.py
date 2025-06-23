import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Assign the constant pi to result
result = mp.pi

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))