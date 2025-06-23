import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Retrieve the Catalan constant (denoted by G in mathematical contexts)
catalan_constant = mp.catalan

# Compute the expression: 2 * π * Catalan_constant
result = 2 * mp.pi * catalan_constant

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))