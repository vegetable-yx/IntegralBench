import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π squared divided by 4
pi_squared_over_4 = mp.power(mp.pi, 2) / 4

# Calculate (ln 2) squared and multiply by 2
ln2 = mp.log(2)
ln2_squared_times2 = 2 * mp.power(ln2, 2)

# Combine results using the analytical expression
result = pi_squared_over_4 - ln2_squared_times2

# Print the final result with 10 decimal places precision
print(mp.nstr(result, n=10))