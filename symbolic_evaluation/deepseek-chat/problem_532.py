import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Multiply by 3
three_pi_squared = 3 * pi_squared

# Divide by 4 to get the final result
result = three_pi_squared / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))