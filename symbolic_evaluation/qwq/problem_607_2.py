import mpmath as mp

mp.dps = 15  # Set decimal places for internal calculations

# Calculate π using mpmath's constant
pi_value = mp.pi

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute π/2
pi_over_two = pi_value / 2

# Multiply components to get final result
result = pi_over_two * ln2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))