import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate pi squared
pi_val = mp.pi
pi_squared = pi_val ** 2

# Divide by 4 to get the final result
result = pi_squared / 4

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))