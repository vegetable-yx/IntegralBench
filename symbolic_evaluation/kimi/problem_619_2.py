import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate the value of pi squared
pi_squared = mp.pi ** 2

# Divide by 8 to obtain the result
result = pi_squared / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))