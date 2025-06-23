import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate each component separately
# pi divided by 4
pi_over_4 = mp.pi / 4

# sqrt(2) divided by 2
sqrt2_over_2 = mp.sqrt(2) / 2

# Compute inner expression: 1 + pi/4 - sqrt(2)/2
inner_expr = 1 + pi_over_4 - sqrt2_over_2

# Multiply by 1/2 to get final result
result = 0.5 * inner_expr

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))