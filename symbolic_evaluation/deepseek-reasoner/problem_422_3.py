import mpmath as mp
mp.dps = 15

# Calculate base 2
base = mp.mpf(2)

# Calculate exponent 4/3
exponent = mp.mpf(4) / mp.mpf(3)

# Compute 2 raised to the 4/3 power
power_result = base ** exponent

# Divide by 4 to get final result
result = power_result / mp.mpf(4)

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))