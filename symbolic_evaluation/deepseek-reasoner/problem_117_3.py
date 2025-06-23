import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π^4
pi_power_4 = pi_value**4

# Divide by 64 to get final result
result = pi_power_4 / 64

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))