import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Multiply by 16
numerator = 16 * pi_squared

# Divide by 105 to get final result
result = numerator / 105

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))