import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Compute pi raised to the fourth power
pi_power = mp.power(pi_val, 4)

# Divide the result by 8 to get final value
result = pi_power / 8

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))