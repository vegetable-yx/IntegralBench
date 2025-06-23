import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 2^(1/4) using exact fractional exponent
base = 2
exponent = mp.mpf(1)/4
two_power = mp.power(base, exponent)

# Multiply by pi to get final result
result = mp.pi * two_power

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))