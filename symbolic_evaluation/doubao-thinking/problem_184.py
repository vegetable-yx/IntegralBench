import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Compute π/8
pi_over_8 = pi_value / 8

# Multiply components to get final result
result = pi_over_8 * ln3

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))