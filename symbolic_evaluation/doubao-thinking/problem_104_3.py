import mpmath as mp
mp.dps = 15

# Calculate square root component
sqrt_15 = mp.sqrt(15)
sqrt_term = sqrt_15 / 2

# Calculate arcsin component
asin_arg = mp.mpf(1)/4
asin_component = mp.asin(asin_arg)
arcsin_term = 7 * asin_component

# Combine components for final result
result = sqrt_term - arcsin_term

print(mp.nstr(result, n=10))