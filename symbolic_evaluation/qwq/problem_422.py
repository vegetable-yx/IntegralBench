import mpmath as mp
mp.dps = 15

# Calculate 2^(4/3) using mpmath precision
base = mp.mpf(2)
exponent = mp.mpf(4)/3
power_result = base ** exponent

# Divide by 4 to get final value
result = power_result / mp.mpf(4)

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))