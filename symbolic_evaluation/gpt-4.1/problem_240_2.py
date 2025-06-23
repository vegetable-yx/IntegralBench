import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate the first term: ln(3 + 2*sqrt(2))
inner_sqrt = mp.sqrt(2)  # Compute sqrt(2)
inner_expr = 3 + 2 * inner_sqrt  # Compute 3 + 2*sqrt(2)
term1 = mp.log(inner_expr)  # Natural logarithm of the expression

# Calculate the second term: pi / (32 * sqrt(2))
denominator = 32 * inner_sqrt  # Compute 32*sqrt(2) (reusing inner_sqrt)
term2 = mp.pi / denominator  # Compute pi / (32*sqrt(2))

# Final result: term1 minus term2
result = term1 - term2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))