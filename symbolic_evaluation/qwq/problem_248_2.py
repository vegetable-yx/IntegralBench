import mpmath as mp

mp.dps = 15  # Set internal precision

# Compute π using mpmath's constant
pi_value = mp.pi

# Compute natural logarithm of 2
ln2_value = mp.log(2)

# Calculate π/2
half_pi = pi_value / 2

# Multiply π/2 with ln(2) to get final result
result = half_pi * ln2_value

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))