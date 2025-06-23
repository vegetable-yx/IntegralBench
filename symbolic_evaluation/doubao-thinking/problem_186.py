import mpmath as mp
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 32 to get final result
result = pi_squared / 32

print(mp.nstr(result, n=10))