import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute ln(2) using mp.log
ln2 = mp.log(2)

# Compute the square of ln(2)
ln2_squared = ln2**2

# Compute the inner expression: -6 + 7*ln(2) + 2*(ln(2))^2
inner_expr = -6 + 7*ln2 + 2*ln2_squared

# Multiply by sqrt(2)
result = mp.sqrt(2) * inner_expr

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))