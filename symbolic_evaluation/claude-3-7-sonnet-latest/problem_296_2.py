import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute pi squared
pi_squared = mp.pi ** 2

# Divide by 16 to get the result
result = pi_squared / 16

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))