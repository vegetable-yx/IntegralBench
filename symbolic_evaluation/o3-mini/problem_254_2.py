import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant pi
pi_value = mp.pi

# Multiply pi by 3
three_pi = 3 * pi_value

# Negate the result to get -3*pi
result = -three_pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))