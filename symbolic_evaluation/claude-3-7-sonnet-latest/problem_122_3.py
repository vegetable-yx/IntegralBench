import mpmath as mp

# Set decimal places for internal computation
mp.dps = 15

# Calculate the constant pi squared
pi_squared = mp.pi ** 2

# Divide by 2 to obtain the result
result = pi_squared / 2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))