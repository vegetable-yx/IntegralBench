import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Assign the constant pi to result
result = mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))