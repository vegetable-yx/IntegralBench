import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate (ln 2)^2 component
ln2 = mp.log(2)
ln2_squared = ln2 ** 2
term1 = ln2_squared / 4

# Calculate π² component
pi_squared = mp.pi ** 2
term2 = pi_squared / 48

# Combine terms for final result
result = term1 + term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))