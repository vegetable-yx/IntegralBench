import mpmath as mp

# Set internal precision to 15 decimal places for calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_val = mp.pi

# Compute π raised to the 4th power
pi_power4 = pi_val**4

# Divide the result by 128
result = pi_power4 / 128

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))