import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi
pi_value = mp.pi

# Square pi
pi_squared = mp.power(pi_value, 2)

# Divide by 4 to obtain the result
result = pi_squared / 4

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))