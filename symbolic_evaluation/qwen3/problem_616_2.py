import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate (ln2)^2 component
ln2 = mp.log(2)
ln2_squared = ln2 ** 2

# Calculate first term: (ln2)^2 / 4
term1 = ln2_squared / 4

# Calculate pi^2 component
pi_squared = mp.pi ** 2

# Calculate second term: pi^2 / 48
term2 = pi_squared / 48

# Combine terms for final result
result = term1 + term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))