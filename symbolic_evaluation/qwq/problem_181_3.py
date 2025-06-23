import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate sin(2) and divide by 2
term1 = mp.sin(2) / 2

# Calculate cos(2)
term2 = mp.cos(2)

# Compute the inner expression (sin(2)/2 - cos(2))
inner_expr = term1 - term2

# Square the inner expression
squared = inner_expr ** 2

# Divide by pi to get the final result
result = squared / mp.pi

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))