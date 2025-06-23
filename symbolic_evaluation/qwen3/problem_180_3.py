import mpmath as mp
mp.dps = 15

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Divide by 2 to get final result
result = sqrt_2 / 2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))