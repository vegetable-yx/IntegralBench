import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the fraction 4/3
fraction = mp.mpf(4) / mp.mpf(3)

# Compute natural logarithm of the fraction (ln(4/3))
log_val = mp.log(fraction)

# Multiply the logarithm by 5
five_log = 5 * log_val

# Subtract 1 from the result
inner_expr = five_log - 1

# Multiply by pi/4 to get the final result
result = (mp.pi / 4) * inner_expr

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))