import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 6
sqrt6 = mp.sqrt(6)

# Compute the expression inside parentheses: 3 - sqrt(6)
inner_expr = 3 - sqrt6

# Multiply by pi and then divide by 12
result = (mp.pi * inner_expr) / 12

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))