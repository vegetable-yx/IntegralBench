import mpmath as mp

# Set internal decimal precision to 15 digits for intermediate calculations
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 2 to get the result
result = pi_squared / 2

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))