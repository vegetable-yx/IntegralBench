import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the term (3 - 2*sqrt(2))
inner_term = 3 - 2 * sqrt2

# Multiply by 3 and then by pi
result = 3 * mp.pi * inner_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))