import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute the value of pi using mpmath's constant
pi_value = mp.pi

# Divide pi by 8 to get the result
result = pi_value / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))