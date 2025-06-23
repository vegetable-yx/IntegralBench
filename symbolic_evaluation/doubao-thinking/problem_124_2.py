import mpmath as mp

mp.dps = 15  # Set internal decimal precision

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Square the value of pi
pi_squared = mp.power(pi_value, 2)

# Divide the squared pi by 16 to get the result
result = mp.fdiv(pi_squared, 16)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))