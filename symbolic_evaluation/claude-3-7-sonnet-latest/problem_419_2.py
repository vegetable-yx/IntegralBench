import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 6 to get the result
result = pi_squared / 6

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))