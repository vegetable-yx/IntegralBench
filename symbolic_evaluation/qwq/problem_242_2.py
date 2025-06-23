import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π and cube it
pi_value = mp.pi
pi_cubed = pi_value ** 3

# Calculate denominator components
sqrt3 = mp.sqrt(3)
denominator = 3 * sqrt3

# Compute final result
result = pi_cubed / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))