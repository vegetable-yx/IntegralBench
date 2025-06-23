import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π raised to the fourth power
pi_power_4 = pi_value ** 4

# Calculate the denominator
denominator = 144

# Compute the final result by dividing π^4 by 144
result = pi_power_4 / denominator

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))