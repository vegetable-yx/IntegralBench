import mpmath as mp

# Set internal decimal precision to 15 for accurate results
mp.dps = 15

# Calculate the square root of 5
sqrt5 = mp.sqrt(5)

# Compute the reciprocal of sqrt(5)
inv_sqrt5 = 1 / sqrt5

# Calculate the term (1 - 1/sqrt(5))
inner_term = 1 - inv_sqrt5

# Multiply by pi/2
result = (mp.pi / 2) * inner_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))