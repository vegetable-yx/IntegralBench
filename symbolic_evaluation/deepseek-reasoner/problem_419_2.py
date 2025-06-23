import mpmath as mp
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Divide by 6 to get the final result
result = pi_sq / 6

print(mp.nstr(result, n=10))