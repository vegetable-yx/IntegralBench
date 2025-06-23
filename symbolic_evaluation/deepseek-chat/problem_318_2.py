import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate 1 over square root of 2
inv_sqrt2 = 1 / mp.sqrt(2)

# Compute the term (1 - 1/sqrt(2))
inner_term = 1 - inv_sqrt2

# Multiply by pi/2
result = (mp.pi / 2) * inner_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))