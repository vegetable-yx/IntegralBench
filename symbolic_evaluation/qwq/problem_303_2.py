import mpmath as mp
mp.dps = 15

# Calculate arcsin(1/4)
arcsin_value = mp.asin(0.25)

# Square the arcsin result
arcsin_squared = arcsin_value ** 2

# Multiply by pi
pi_times_squared = mp.pi * arcsin_squared

# Divide by 32 to get final result
result = pi_times_squared / 32

print(mp.nstr(result, n=10))