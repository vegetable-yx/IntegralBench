import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute π squared
pi_squared = mp.pi ** 2

# Divide π squared by 6
pi_squared_over_6 = pi_squared / 6

# Subtract 1 from the result
result = pi_squared_over_6 - 1

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))