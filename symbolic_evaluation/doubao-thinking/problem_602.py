import mpmath as mp
mp.dps = 15

# Calculate pi^4 using mpmath's constant
pi_power_4 = mp.pi ** 4

# Divide the result by 120 to get the final value
result = pi_power_4 / 120

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))