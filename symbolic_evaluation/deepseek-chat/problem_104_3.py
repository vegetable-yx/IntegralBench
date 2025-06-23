import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 16 to get the first term
term1 = pi_squared / 16

# Subtract 1/2 to get the final result
result = term1 - 0.5

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))