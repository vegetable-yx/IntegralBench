import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_val = mp.pi

# Square the π value
pi_squared = mp.power(pi_val, 2)

# Divide squared π by 4
pi_squared_over_4 = mp.fdiv(pi_squared, 4)

# Apply negative sign to get final result
result = mp.fneg(pi_squared_over_4)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))