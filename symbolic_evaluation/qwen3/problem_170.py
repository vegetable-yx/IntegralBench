import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the square root of 15
sqrt_15 = mp.sqrt(15)

# Calculate arcsin(1/4) using mp.asin
arcsin_val = mp.asin(1/4)

# Combine terms: √15 + arcsin(1/4) - 4
inner_expr = sqrt_15 + arcsin_val - 4

# Multiply by π/2
result = (mp.pi / 2) * inner_expr

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))