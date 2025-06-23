import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π²/6
pi_squared_over_6 = mp.pi**2 / 6

# Calculate (ln 2)²
ln2 = mp.log(2)
ln2_squared = ln2**2

# Compute final result by subtracting terms
result = pi_squared_over_6 - ln2_squared

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))