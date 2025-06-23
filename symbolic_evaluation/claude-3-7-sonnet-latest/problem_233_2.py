import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by pi
result = mp.pi * sqrt2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))