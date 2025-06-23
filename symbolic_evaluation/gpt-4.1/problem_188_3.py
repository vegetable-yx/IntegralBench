import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 32 to get the result
result = pi_squared / 32

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))