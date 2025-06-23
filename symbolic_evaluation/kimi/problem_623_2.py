import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π/2 using mpmath's constant
pi_half = mp.pi / 2

# Calculate natural logarithm of 2
ln_2 = mp.log(2)

# Multiply the components to get final result
result = pi_half * ln_2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))