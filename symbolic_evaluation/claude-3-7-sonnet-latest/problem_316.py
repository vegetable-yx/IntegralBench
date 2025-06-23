import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Multiply by 2
two_pi_squared = 2 * pi_squared

# Divide by 3 to get the final result
result = two_pi_squared / 3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))