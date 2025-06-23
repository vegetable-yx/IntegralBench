import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute arcsin(0.5) using mpmath's asin function
arcsin_val = mp.asin(0.5)

# Compute π/8
pi_over_8 = mp.pi / 8

# Multiply the components to get the final result
result = pi_over_8 * arcsin_val

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))