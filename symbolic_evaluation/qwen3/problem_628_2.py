import mpmath as mp
mp.dps = 15

# Calculate numerator components
pi_value = mp.pi
constant_term = mp.mpf(2)

# Compute 2 + π
numerator = constant_term + pi_value

# Divide by 8 and apply negative sign
result = -numerator / 8

print(mp.nstr(result, n=10))