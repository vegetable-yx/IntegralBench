import mpmath as mp
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Square the result to get pi^4
pi_fourth = pi_squared ** 2

# Divide by 2048 to obtain final value
result = pi_fourth / 2048

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))