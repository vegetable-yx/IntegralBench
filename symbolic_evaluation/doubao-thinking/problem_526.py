import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi = mp.pi

# Calculate π/4
pi_over_4 = pi / 4

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Multiply the components to get final result
result = pi_over_4 * ln3

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))