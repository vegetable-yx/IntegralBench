import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the components of the expression
# First: compute 1/sqrt(2)
inv_sqrt2 = 1 / mp.sqrt(2)

# Second: compute (1 - 1/sqrt(2))
inner_expr = 1 - inv_sqrt2

# Third: multiply by pi/2
result = (mp.pi / 2) * inner_expr

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))