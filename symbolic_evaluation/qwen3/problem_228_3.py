import mpmath as mp

mp.dps = 15  # Set decimal places for internal calculations

# Calculate sqrt(2)
sqrt_2 = mp.sqrt(2)

# Compute the argument for logarithm: 1 + sqrt(2)
log_arg = 1 + sqrt_2

# Calculate natural logarithm of (1 + sqrt(2))
ln_value = mp.log(log_arg)

# Square the logarithm value
ln_squared = ln_value ** 2

# Calculate pi squared
pi_sq = mp.pi ** 2

# Combine all components: (pi^2 * ln^2(1+sqrt(2))) / 8
result = (pi_sq * ln_squared) / 8

# Print result with 10 decimal places
print(mp.nstr(result, n=10))