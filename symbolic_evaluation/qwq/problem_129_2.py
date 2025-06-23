import mpmath as mp
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Calculate e squared
e_squared = mp.exp(2)

# Multiply components to get final result
result = sqrt2 * e_squared

print(mp.nstr(result, n=10))