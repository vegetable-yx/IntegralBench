import mpmath as mp
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Square the π value
pi_squared = mp.power(pi_value, 2)

# Divide by 512 to get final result
result = mp.fdiv(pi_squared, 512)

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))