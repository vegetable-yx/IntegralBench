import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute the square root of 2
result = mp.sqrt(2)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))