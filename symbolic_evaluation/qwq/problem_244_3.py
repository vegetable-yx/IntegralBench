import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π using mpmath's constant
pi_val = mp.pi

# Compute π raised to the fourth power
pi_power4 = pi_val**4

# Calculate the final result using the formula (3/8)π⁴
result = (mp.mpf(3)/8) * pi_power4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))