import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate π^3
pi_cubed = mp.pi ** 3

# Compute first term: π^3 / 48
term1 = pi_cubed / 48

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Square the logarithm of 2
ln2_squared = ln2 ** 2

# Compute second term: (π/4) * (ln^2 2)
term2 = (mp.pi / 4) * ln2_squared

# Sum both terms to get final result
result = term1 + term2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))