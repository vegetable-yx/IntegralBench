import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate each term of the expression separately
pi_squared_over_3 = mp.pi**2 / 3  # Compute π²/3
constant_term = -8  # Constant term -8
ln2 = mp.log(2)  # Natural logarithm of 2
eight_ln2 = 8 * ln2  # 8 multiplied by ln(2)
ln2_squared = ln2**2  # Square of ln(2)
four_ln2_sq = 4 * ln2_squared  # 4 multiplied by (ln2)²

# Combine all terms to get the final result
result = pi_squared_over_3 + constant_term + eight_ln2 - four_ln2_sq

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))