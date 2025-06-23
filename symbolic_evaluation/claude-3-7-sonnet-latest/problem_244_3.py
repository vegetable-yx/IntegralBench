import mpmath as mp

# Set internal decimal precision to 15 for accurate intermediate calculations
mp.dps = 15

# Compute pi to the fourth power
pi_power_4 = mp.pi ** 4

# Multiply by 3
numerator = 3 * pi_power_4

# Divide by 32 to get the final result
result = numerator / 32

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))