import mpmath as mp
mp.dps = 15

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Multiply by pi to get the numerator
pi_times_sqrt3 = mp.pi * sqrt3

# Divide by 9 to get the final result
result = pi_times_sqrt3 / 9

print(mp.nstr(result, n=10))