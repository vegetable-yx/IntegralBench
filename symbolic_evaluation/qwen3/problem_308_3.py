import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 1/sqrt(2)
one_over_sqrt2 = mp.mpf(1)/mp.sqrt(2)

# Compute arctan(1/sqrt(2))
arctan_term = mp.atan(one_over_sqrt2)

# Multiply the arctan result by 3
three_arctan = 3 * arctan_term

# Calculate sqrt(2)
sqrt2 = mp.sqrt(2)

# Final calculation: 3*arctan(1/sqrt(2)) - sqrt(2)
result = three_arctan - sqrt2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))