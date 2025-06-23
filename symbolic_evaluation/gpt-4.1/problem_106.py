import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate pi squared
pi_squared = mp.power(mp.pi, 2)

# Divide by 6 to obtain the result
result = pi_squared / 6

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))