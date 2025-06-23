import mpmath as mp
mp.dps = 15

from mpmath import mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate 2 raised to the power of 4/3
base = mp.mpf(2)
exponent = mp.mpf(4) / mp.mpf(3)
power_result = base ** exponent

# Multiply by 1/4
result = mp.mpf(1) / mp.mpf(4) * power_result

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))