import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide pi squared by 16 to get the result
result = pi_squared / 16

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))