import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Compute the Struve function of order 1 at the point 1
struve_value = mp.struveh(1, 1)

# Compute the expression (1 - Struve function)
one_minus_struve = 1 - struve_value

# Multiply by pi to get the final result
result = mp.pi * one_minus_struve

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))