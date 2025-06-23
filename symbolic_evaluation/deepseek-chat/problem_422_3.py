import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate 2 raised to the power of 4/3
base = mp.mpf(2)
exponent = mp.mpf(4)/3
power_result = mp.power(base, exponent)

# Divide the result by 4
result = power_result / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))