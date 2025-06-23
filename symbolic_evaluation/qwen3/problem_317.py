import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Calculate pi squared
pi_squared = mp.pi ** 2

# Multiply sqrt(2) by pi squared
numerator = sqrt2 * pi_squared

# Divide by 4 to get final result
result = numerator / 4

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))