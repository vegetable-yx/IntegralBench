import mpmath as mp

# Set internal decimal precision to 15 digits for intermediate calculations
mp.dps = 15

# Compute pi squared
pi_squared = mp.pi ** 2

# Divide by 24 to get the result
result = pi_squared / 24

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))