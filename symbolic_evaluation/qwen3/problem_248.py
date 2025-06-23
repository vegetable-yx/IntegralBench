import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Compute π/4 component
pi_over_4 = mp.pi / 4

# Compute natural logarithm of 2
ln_2 = mp.log(2)

# Multiply components to get final result
result = pi_over_4 * ln_2

print(mp.nstr(result, n=10))