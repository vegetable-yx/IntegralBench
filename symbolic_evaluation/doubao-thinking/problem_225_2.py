import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Square the value of pi
pi_squared = mp.power(pi_value, 2)

# Divide the squared pi by 2
result = pi_squared / 2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))