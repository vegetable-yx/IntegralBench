import mpmath as mp
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Square the result to get pi to the fourth power
pi_fourth = pi_squared ** 2

# Divide by 120 to get final result
result = pi_fourth / 120

# Print with 10 decimal precision
print(mp.nstr(result, n=10))