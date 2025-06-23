import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π (using mpmath's built-in constant)
pi_val = mp.pi

# Compute π raised to the 4th power
pi_power_4 = mp.power(pi_val, 4)

# Divide π^4 by 120 to get the final result
result = pi_power_4 / 120

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))