import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Compute pi raised to the fourth power
pi_power4 = pi_value ** 4

# Divide by 120 to get the final result
result = pi_power4 / 120

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))