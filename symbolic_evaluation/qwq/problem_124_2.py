import mpmath as mp
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Square the result to get pi^4
pi_fourth = pi_squared ** 2

# Divide by 192 to get final result
result = pi_fourth / 192

print(mp.nstr(result, n=10))