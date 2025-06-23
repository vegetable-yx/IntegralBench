import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Multiply by 5
five_pi_squared = 5 * pi_squared

# Divide by 4 to get the final result
result = five_pi_squared / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))