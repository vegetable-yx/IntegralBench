import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate intermediate values
sqrt5 = mp.sqrt(5)   # sqrt(5)
inner_expr = 5 - 2 * sqrt5   # (5 - 2*sqrt(5))
numerator = mp.pi * inner_expr   # π*(5-2*sqrt(5))
denominator = 2 * sqrt5   # 2*sqrt(5)

# Compute the final result
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))