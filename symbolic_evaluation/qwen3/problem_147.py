import mpmath as mp
mp.dps = 15

# Calculate π squared
pi_sq = mp.pi ** 2

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply π squared by sqrt(2)
product = pi_sq * sqrt2

# Divide by 2 to get final result
result = product / 2

print(mp.nstr(result, n=10))