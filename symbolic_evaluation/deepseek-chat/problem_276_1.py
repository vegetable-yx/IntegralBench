import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign the mathematical constant pi
result = mp.pi

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))