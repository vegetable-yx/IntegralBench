import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Multiply by 4
four_pi_squared = 4 * pi_squared

# Divide by 3 to get the result
result = four_pi_squared / 3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))