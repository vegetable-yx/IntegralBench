import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_squared = mp.power(mp.pi, 2)

# Divide by 6
basel_term = pi_squared / 6

# Subtract 1 to get the final result
result = basel_term - 1

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))