import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Square the pi value
pi_squared = mp.power(pi_value, 2)

# Divide by 9 to get final result
result = pi_squared / 9

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))