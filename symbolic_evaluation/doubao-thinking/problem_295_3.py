import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Square the calculated pi
pi_squared = mp.power(pi_value, 2)

# Divide the squared pi by 16 to get the final result
result = mp.fdiv(pi_squared, 16)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))