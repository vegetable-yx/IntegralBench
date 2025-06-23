import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 9 to obtain the result
result = pi_squared / 9

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))