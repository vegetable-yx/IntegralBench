import mpmath as mp
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Square pi squared to get pi^4
pi_fourth = pi_squared ** 2

# Divide by 64 to get final result
result = pi_fourth / 64

print(mp.nstr(result, n=10))